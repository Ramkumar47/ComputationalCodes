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

!------------------------------------------------------------------------------

module dense_layer_definitions

    use parameters

    implicit none

    type, public :: dense_layer
        integer(kind=ikd) :: units, input_size
        real(kind=rkd),dimension(:,:),allocatable :: weights
        real(kind=rkd),dimension(:),allocatable :: bias
        real(kind=rkd),dimension(:),allocatable :: input
        real(kind=rkd),dimension(:),allocatable :: z_vector
        character(len=50) :: layer_name
        real(kind=rkd),dimension(:),allocatable :: dSigmadz,dLdz,dLdb
        real(kind=rkd),dimension(:,:),allocatable :: dSigmadx,dLdw
    contains
        procedure :: initialize => layer_initialization
        procedure :: evaluate => layer_evaluation
        procedure :: activate => layer_activation
        procedure :: compute_derivatives => layer_derivatives
        procedure :: save_weights => layer_save_weights
        procedure :: optimize => layer_optimize
    end type dense_layer

contains
    subroutine layer_initialization(self,name,load_weights)
        ! defining arguments
        class(dense_layer), intent(inout) :: self
        character(len=*), intent(in) :: name
        logical, intent(in) :: load_weights
        character(len=50) :: fname
        integer(kind=ikd) :: i,j

        ! allocating weights and biases and other vectors
        allocate(self%weights(self%units,self%input_size))
        allocate(self%bias(self%units))
        allocate(self%input(self%input_size))
        allocate(self%z_vector(self%units))
        allocate(self%dSigmadz(self%units))
        ! allocate(self%dLdz(self%input_size))
        allocate(self%dLdz(self%units))
        allocate(self%dLdb(self%units))
        allocate(self%dLdw(self%units,self%input_size))
        allocate(self%dSigmadx(self%input_size,self%units))

        ! initializing weights and biases
        call random_number(self%weights)
        call random_number(self%bias)

        ! assigning layer name
        self%layer_name = trim(name)

        ! loading weights if insisted
        if (load_weights) then
            ! loading weights
            write(fname, '(A,"/",A,A)') "saved_weights",trim(name),"_weights.csv"
            open(unit = 1, file = fname, status = "old")
            do i = 1,self%units
                do j = 1,self%input_size
                    read(unit=1,fmt=*) self%weights(i,j)
                end do
            end do

            ! loading bias
            write(fname, '(A,"/",A,A)') "saved_weights",trim(name),"_bias.csv"
            open(unit = 1, file = fname, status = "old")
            do i = 1,self%units
                read(unit=1,fmt=*) self%bias(i)
            end do
            print *,trim(self%layer_name)," : loaded weights"
        end if


    end subroutine layer_initialization

    function layer_evaluation(self, x) result (output)
        ! defining arguments
        class(dense_layer), intent(inout) :: self
        real(kind=rkd), dimension(self%input_size), intent(in) :: x
        real(kind=rkd), dimension(self%units) :: output

        ! adding input to the memory
        self%input = x

        ! evaluating output
        output = self%activate(matmul(self%weights,x) + self%bias)

    end function layer_evaluation

    function layer_activation(self,x) result(output)
        ! defining arguments
        class(dense_layer), intent(in) :: self
        real(kind=rkd), dimension(self%units), intent(in) :: x
        real(kind=rkd), dimension(self%units) :: output

        output = tanh(x)

    end function layer_activation

    subroutine layer_derivatives(self)
        ! defining arguments
        class(dense_layer), intent(inout) :: self
        real(kind=rkd), dimension(self%units,self%units) :: eye
        integer(kind=ikd) :: i

        ! computing z vector
        self%z_vector = matmul(self%weights,self%input) + self%bias

        ! computing derivative of output w.r.t. z vector
        self%dSigmadz = 1.0 - tanh(self%z_vector)**2

        ! computing derivative of output w.r.t. input
        eye = 0.0
        do i = 1,self%units
            eye(i,i) = self%dSigmadz(i)
        end do
        self%dSigmadx = matmul(transpose(self%weights),eye)

    end subroutine layer_derivatives

    subroutine layer_save_weights(self)
        ! defining arguments
        class(dense_layer), intent(in) :: self
        character(len=50) :: filename_weights,filename_bias
        integer(kind=ikd) :: i,j

        ! preparing filename to save weights and biases
        write(filename_weights, '(A,"/",A,A)') &
            "saved_weights",trim(self%layer_name),"_weights.csv"
        write(filename_bias, '(A,"/",A,A)') &
            "saved_weights",trim(self%layer_name),"_bias.csv"

        ! preparing save directory
        call system("mkdir -p saved_weights")

        ! saving weights
        open(unit=1,file=filename_weights,status="replace")
        do i = 1, self%units
            do j = 1, self%input_size
                write(unit=1, fmt=*) self%weights(i,j)
            end do
        end do
        close(unit=1)

        ! saving biases
        open(unit=1,file=filename_bias,status="replace")
        do i = 1, self%units
            write(unit=1, fmt=*) self%bias(i)
        end do
        close(unit=1)

        print *,trim(self%layer_name)," : saved weights"

    end subroutine layer_save_weights

    subroutine layer_optimize(self)
        ! defining arguments
        class(dense_layer),intent(inout) :: self
        integer(kind=ikd) :: i,j

        ! computing dLdw
        do i = 1,self%units
            do j = 1,self%input_size
                self%dLdw(i,j) = self%dLdz(i)*self%input(j)
            end do
        end do

        ! computing dLdb
        self%dLdb = self%dLdz*1.0

        ! updating weights and biases
        self%weights = self%weights - beta*self%dLdW
        self%bias   = self%bias - beta*self%dLdb

    end subroutine layer_optimize

end module dense_layer_definitions
