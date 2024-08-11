!------------------------------------------------------------------------------
! single composed neurons curve fit program : modules definition
!------------------------------------------------------------------------------

module neuron_definitions

    use parameters

    implicit none

    ! defining a neuron type
    type, public :: neuron
        real(kind=rkd) :: weight = 1.0
        real(kind=rkd) :: bias = 1.0
        real(kind=rkd) :: input = 0.0
        real(kind=rkd) :: z = 0.0
        real(kind=rkd) :: dsigmadz, dsigmadx
        character(len=50) :: name
    contains
        procedure :: initialize => init_neuron
        procedure :: evaluate => eval_neuron
        procedure :: activate => activate_tanh
        procedure :: save_weights => save_weights_neuron
        procedure :: compute_derivatives => compute_derivatives_neuron
    end type neuron

    ! defining functions and subroutines
contains
    ! evaluation of neuron
    real(kind=rkd) function eval_neuron(self,x) &
            result(val)
        ! defining arguments
        class(neuron), intent(inout) :: self
        real(kind=rkd), intent(in) :: x

        self%input = x

        ! computing evaluation
        self%z = self%weight * x + self%bias

        ! activating output
        val = self%activate(self%z)
    end function eval_neuron

    ! activation function
    pure real(kind=rkd) function activate_tanh(self,x) &
            result(out)
        ! defining arguments
        class(neuron), intent(in) :: self
        real(kind=rkd), intent(in) :: x

        ! computing activation
        out = tanh(x)

    end function activate_tanh

    ! initialization of neuron
    subroutine init_neuron(self,name,load_weights)
        ! defining arguments
        class(neuron), intent(inout) :: self
        logical, intent(in) :: load_weights
        character(len=*), intent(in) :: name
        character(len=50) :: load_fname
        self%name = name

        if (load_weights) then
            ! preparing filename
            write(load_fname,'(A,"/",A,A)') "saved_weights",trim(name),".csv"

            ! reading data
            open(unit=1, file=load_fname, status="old")
            read(unit=1,fmt=*) self%weight,self%bias
            close(unit=1)

        else
            call random_number(self%weight)
            call random_number(self%bias)
        end if
    end subroutine init_neuron

    ! saving weights of trained neuron
    subroutine save_weights_neuron(self)
        ! defining arguments
        class(neuron), intent(in) :: self
        character(len=100) :: filename

        ! preparing filename
        write(filename, '(A,"/",A,A)') "saved_weights",trim(self%name),".csv"

        ! preparing directory
        call system("mkdir -p saved_weights")

        ! writing weights
        open(unit=1, file=filename, status="replace")
        write(unit=1,fmt=*) self%weight,self%bias
        close(unit=1)

    end subroutine save_weights_neuron

    ! computing derivatives
    subroutine compute_derivatives_neuron(self)
        ! defining arguments
        class(neuron), intent(inout) :: self

        ! derivative of tanh
        self%dsigmadz = 1.0 - tanh(self%z)**2
        self%dsigmadx = self%dsigmadz*self%weight

    end subroutine compute_derivatives_neuron

end module neuron_definitions
