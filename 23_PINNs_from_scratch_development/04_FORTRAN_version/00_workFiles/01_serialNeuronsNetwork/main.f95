!------------------------------------------------------------------------------
! single composed neurons curve fit program : main code
!------------------------------------------------------------------------------

program main

    use parameters
    use variables
    use neuron_definitions

    implicit none

    ! preparing dataset
    x = (/(ival/float(N_size-1)/2.0, ival = 0,N_size-1,1)/)
    ! y = x**2
    y = 0.5*sin(4*x)

    ! initializing neurons
    do i = 1,N_neuron
        ! framing name of neuron
        write(dummy_name, "(A,I0.4)") "neuron_",i
        ! initializing neuron
        call neuron_array(i)%initialize(name=trim(dummy_name),load_weights=load_weights)
    end do

    ! training the model
    mainloop: do epoch = 1,N_epochs
        ! looping through each data record
        do ival = 1,N_size
            ! performing forward pass
            tmp = x(ival)
            do i = 1,N_neuron
                tmp = neuron_array(i)%evaluate(tmp)
            end do
            y_pred(ival) = tmp

            ! computing loss value
            lossVal = 1.0/N_size*(y_pred(ival)-y(ival))**2

            ! performing back propagation
            dLdz = 2.0/N_size*(y_pred(ival) - y(ival))
            do i = 1,N_neuron
                ! going in reverse
                j = N_neuron-i+1
                ! computing derivatives
                call neuron_array(j)%compute_derivatives()
                dLdz = dLdz*neuron_array(j)%dsigmadz
                dLdw = dLdz*neuron_array(j)%input
                dLdb = dLdz
                ! updating weights and biases
                neuron_array(j)%weight = neuron_array(j)%weight - beta*dLdw
                neuron_array(j)%bias   = neuron_array(j)%bias - beta*dLdb
            end do

        end do

        print '("epoch = ",I10,"  Loss = ",ES12.6)', epoch, lossVal

    end do mainloop

    ! saving weights of networks
    do i = 1,N_neuron
        call neuron_array(i)%save_weights()
    end do

    ! writing predicted data
    call write_data()

end program main
