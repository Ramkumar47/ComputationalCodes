!------------------------------------------------------------------------------
! Heat condution in 1D plane
!
! file description : main program definition
!------------------------------------------------------------------------------

! main program
program main

    use modelVars
    include "mpif.h"

    ! local variables definition
    logical :: convergenceFlag = .False.

    ! initializing MPI
    call MPI_Init(ierror)

    ! getting current processor id
    call MPI_Comm_rank(mpi_comm_world, proc_id, ierror)

    ! getting number of processors and checking consistency
    call MPI_Comm_size(mpi_comm_world, num_procs_input, ierror)
    ! if (num_procs /= num_procs_input) then
    !     ERROR stop "number of processes must be 2 !"
    ! endif

    ! master process, initializes the field
    if (proc_id == 0) then
        print *, "initializing T field"
        T = 100.0
        T(1) = T_west
        T(Nx) = T_east

        print *,"initializing grid"
        X = 0.0
        do i = 1,Nx
            X(i) = (i-1)*dx
        end do

    endif

    ! scattering the data across 2 processors
    call MPI_scatter(T, N_chunk, MPI_DOUBLE_PRECISION, T_chunk, N_chunk, MPI_DOUBLE_PRECISION, 0, MPI_COMM_WORLD, ierror)
    print *, "scattering data from proc_id : ", proc_id

    ! beginning main loop
    mainloop: do iter = 1, maxIterCount

        ! process 0 definition
        if (proc_id == 0) then

            ! sending the edge value to the other process
            call MPI_send(T_chunk(N_chunk), 1, &
                            MPI_DOUBLE_PRECISION, proc_id+1, &
                            1, MPI_COMM_WORLD, &
                            ierror)

            ! receiving the boundary value from the other process
            call MPI_recv(T_bc, 1, &
                            MPI_DOUBLE_PRECISION, proc_id+1, &
                            1, MPI_COMM_WORLD, &
                            MPI_STATUS_IGNORE, &
                            ierror)

            ! adding the bc to field array
            T_chunk_bc = [T_chunk, T_bc]

            ! computing field values
            do i = 2,N_chunk
                T_chunk(i) = (T_chunk_bc(i+1) + T_chunk_bc(i-1))/2.0 + Q_source*dx**2/2.0/k
            end do

            ! ! receiving residual from the other process
            ! call MPI_recv(conv_res_1, 1, MPI_DOUBLE_PRECISION, 1, 1000, MPI_COMM_WORLD, MPI_STATUS_IGNORE, ierror)
            !
            ! ! computing residual
            ! convergence_residual = max(conv_res_1, maxval(abs(T_chunk - T_chunk_bc(:N_chunk))))

            convergence_residual = maxval(abs(T_chunk - T_chunk_bc(:N_chunk)))

            ! print status
            print *,"iteration : ", iter,"; residual = ",convergence_residual
        endif

        ! process last definition
        if (proc_id == num_procs-1) then

            ! sending the edge value to the other process
            call MPI_send(T_chunk(1), 1, &
                        MPI_DOUBLE_PRECISION, proc_id-1, &
                        1, MPI_COMM_WORLD, &
                        ierror)

            ! receiving the boundary value from the other process
            call MPI_recv(T_bc, 1, &
                        MPI_DOUBLE_PRECISION, proc_id-1, &
                        1, MPI_COMM_WORLD, MPI_STATUS_IGNORE, &
                        ierror)

            ! adding the bc to field array
            T_chunk_bc = [T_bc, T_chunk]

            ! computing field values
            do i = 2,N_chunk
                T_chunk(i-1) = (T_chunk_bc(i+1) + T_chunk_bc(i-1))/2.0 + Q_source*dx**2/2.0/k
            end do

            ! computing residual
            convergence_residual = maxval(abs(T_chunk - T_chunk_bc(2:)))

            ! sending residual to main process
            call MPI_send(convergence_residual, 1, MPI_DOUBLE_PRECISION, 0, 1000, MPI_COMM_WORLD, ierror)

        endif

        ! intermediate processes
        if (proc_id > 0 .and. proc_id < num_procs -1) then
            ! sending the left edge value to the left side process
            call MPI_send(T_chunk(1), 1, &
                        MPI_DOUBLE_PRECISION, proc_id-1, &
                        1, MPI_COMM_WORLD, &
                        ierror)

            ! receiving the boundary value from the left side process
            call MPI_recv(T_bcl, 1, &
                        MPI_DOUBLE_PRECISION, proc_id-1, &
                        1, MPI_COMM_WORLD, MPI_STATUS_IGNORE, &
                        ierror)

            ! sending the right edge value to the right side process
            call MPI_send(T_chunk(N_chunk), 1, &
                        MPI_DOUBLE_PRECISION, proc_id+1, &
                        1, MPI_COMM_WORLD, &
                        ierror)

            ! receiving the boundary value from the left side process
            call MPI_recv(T_bcr, 1, &
                        MPI_DOUBLE_PRECISION, proc_id+1, &
                        1, MPI_COMM_WORLD, MPI_STATUS_IGNORE, &
                        ierror)
            ! adding the bc to field array
            T_chunk_bc2 = [T_bcl, T_chunk, T_bcr]

            ! computing field values
            do i = 2,N_chunk+1
                T_chunk(i-1) = (T_chunk_bc2(i+1) + T_chunk_bc2(i-1))/2.0 + Q_source*dx**2/2.0/k
            end do

            ! computing residual
            convergence_residual = maxval(abs(T_chunk - T_chunk_bc2(2:N_chunk+1)))

        end if

        ! if (convergence_residual < convergence_value) then
        !     print *,"solution converged"
        !     ! exit mainloop
        ! endif

    end do mainloop

    ! gathering computed data
    call MPI_gather(T_chunk, N_chunk, MPI_DOUBLE_PRECISION, T, N_chunk, MPI_DOUBLE_PRECISION, 0, MPI_COMM_WORLD, ierror)

    if (proc_id == 0) then
        call write_csv()
        print *,"End"
    endif

    ! finalizing MPI
    call MPI_FINALIZE(ierror)

end program main
