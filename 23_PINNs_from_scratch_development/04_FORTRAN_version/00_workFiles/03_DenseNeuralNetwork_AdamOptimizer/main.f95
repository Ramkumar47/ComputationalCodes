!------------------------------------------------------------------------------
! single composed neurons curve fit program : main code
!------------------------------------------------------------------------------

program main

    use parameters
    use variables

    implicit none

    ! reading dataset
    call read_training_data()

    ! initializing dense layers
    dense_layer_array(1)%input_size = input_size
    dense_layer_array(1)%units = layers(1)
    write(dummy_name,"(A,I0.2)") "layer_",1
    call dense_layer_array(1)%initialize(name=trim(dummy_name), &
        load_weights = load_weights)
    do i = 2,N_layer
        ! framing name of neuron
        write(dummy_name, "(A,I0.2)") "layer_",i
        ! assiging shapes
        dense_layer_array(i)%input_size = dense_layer_array(i-1)%units
        dense_layer_array(i)%units = layers(i)
        ! initializing neuron
        call dense_layer_array(i)%initialize(name=trim(dummy_name), &
            load_weights = load_weights)
    end do

    ! training the model
    mainloop: do epoch = 1,N_epochs
        ! looping through each data record
        evaluation: do ival = 1,N_data
            ! performing forward pass
            dense_layer_array(1)%input = x(ival)
            call dense_layer_array(1)%evaluate()
            do i = 2,N_layer
                dense_layer_array(i)%input = dense_layer_array(i-1)%output
                call dense_layer_array(i)%evaluate()
            end do
            ! getting last value to y_pred
            y_pred(ival) = dense_layer_array(N_layer)%output(1)
        end do evaluation

        ! computing loss value
        lossVal = 1.0/N_data*sum((y_pred-y)**2)

        ! performing back propagation for the last layer
        dLdsigma = 2.0/N_data*sum(y_pred-y)
        call dense_layer_array(N_layer)%compute_derivatives()
        dense_layer_array(N_layer)%dLdz = dLdsigma*dense_layer_array(N_layer)%dSigmadz
        call dense_layer_array(N_layer)%optimize()
        backpropagation: do i = 2,N_layer
            ! going in reverse
            j = N_layer-i+1
            ! computing derivatives
            call dense_layer_array(j)%compute_derivatives()
            dense_layer_array(j)%dLdz = matmul(transpose(dense_layer_array(j+1)%weights), &
                dense_layer_array(j+1)%dLdz)*dense_layer_array(j)%dSigmadz
            ! optimizing weights and biases
            call dense_layer_array(j)%optimize()
        end do backpropagation

        ! print '("epoch = ",I10,"  Loss = ",ES12.6)', epoch, sum(lossVal)
        print *, epoch, sum(lossVal), dLdsigma

    end do mainloop

    ! saving weights of networks
    call system("rm -rf saved_weights")
    call system("mkdir saved_weights")
    if (save_weights) then
        do i = 1,N_layer
            call dense_layer_array(i)%save_weights()
        end do
    end if

    ! predicting the output
    prediction: do ival = 1,N_data
        ! performing forward pass
        dense_layer_array(1)%input = x(ival)
        call dense_layer_array(1)%evaluate()
        do i = 2,N_layer
            dense_layer_array(i)%input = dense_layer_array(i-1)%output
            call dense_layer_array(i)%evaluate()
        end do
        ! getting last value to y_pred
        y_pred(ival) = dense_layer_array(N_layer)%output(1)
    end do prediction

    ! ! predicting the output
    ! prediction: do ival = 1,N_data
    !     ! performing forward pass
    !     allocate(tmp2(input_size))
    !     tmp2 = x(ival)
    !     do i = 1,N_layer
    !         allocate(tmp1(dense_layer_array(i)%units))
    !         tmp1 = dense_layer_array(i)%evaluate(tmp2)
    !         deallocate(tmp2)
    !         allocate(tmp2(size(tmp1)))
    !         tmp2 = tmp1
    !         deallocate(tmp1)
    !     end do
    !     ! getting last value to y_pred
    !     ! y_pred(ival) = tmp2(layers(size(layers)))
    !     y_pred(ival) = tmp2(1)
    !     deallocate(tmp2)
    ! end do prediction

    ! writing predicted data
    call write_data()

end program main
