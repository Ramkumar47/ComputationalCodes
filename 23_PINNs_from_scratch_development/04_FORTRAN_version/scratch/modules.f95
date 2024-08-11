!------------------------------------------------------------------------------
! dense layer definition module
!------------------------------------------------------------------------------

module dense_layer_definitions

    use parameters

    implicit none

    type, public :: dense_layer
        integer(kind=ikd) :: units, input_size
        real(kind=rkd),dimension(:,:),allocatable :: weights
        real(kind=rkd),dimension(:),allocatable :: bias
        real(kind=rkd),dimension(:),allocatable :: input,output
        real(kind=rkd),dimension(:),allocatable :: z_vector
        character(len=50) :: layer_name
        real(kind=rkd),dimension(:),allocatable :: dSigmadz,dLdz,dLdb
        real(kind=rkd),dimension(:),allocatable :: mb_1,mb,vb_1,vb,mb_bar,vb_bar
        real(kind=rkd),dimension(:,:),allocatable :: dSigmadx,dLdw
        real(kind=rkd),dimension(:,:),allocatable :: mw_1,mw,vw_1,vw,mw_bar,vw_bar
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
        real(kind=rkd),dimension(self%units,self%input_size) :: wgt2
        real(kind=rkd),dimension(self%units) :: bias2

        ! pi value
        real(kind=rkd), parameter :: pi = 4.0*atan(1.0)

        ! allocating weights and biases and other vectors
        allocate(self%weights(self%units,self%input_size))
        allocate(self%bias(self%units))
        allocate(self%input(self%input_size))
        allocate(self%output(self%units))
        allocate(self%z_vector(self%units))
        allocate(self%dSigmadz(self%units))
        allocate(self%dLdz(self%units))
        allocate(self%dLdb(self%units))
        allocate(self%mb_1(self%units))
        allocate(self%vb_1(self%units))
        allocate(self%mb(self%units))
        allocate(self%vb(self%units))
        allocate(self%mb_bar(self%units))
        allocate(self%vb_bar(self%units))
        allocate(self%dLdw(self%units,self%input_size))
        allocate(self%mw_1(self%units,self%input_size))
        allocate(self%mw(self%units,self%input_size))
        allocate(self%vw_1(self%units,self%input_size))
        allocate(self%vw(self%units,self%input_size))
        allocate(self%mw_bar(self%units,self%input_size))
        allocate(self%vw_bar(self%units,self%input_size))
        allocate(self%dSigmadx(self%input_size,self%units))

        ! initializing weights and biases
        call random_number(self%weights)
        call random_number(wgt2)
        call random_number(self%bias)
        call random_number(bias2)

        ! computing random normal values
        self%weights = sqrt(-2.0*log(self%weights))*cos(2.0*pi*wgt2)
        self%bias    = sqrt(-2.0*log(self%bias))*cos(2.0*pi*bias2)

        ! initializing momentum variables for adam optimziation algorithm
        self%mw_1 = 0.0
        self%mb_1 = 0.0
        self%vw_1 = 0.0
        self%vb_1 = 0.0

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

    subroutine layer_evaluation(self)
        ! defining arguments
        class(dense_layer), intent(inout) :: self

        ! evaluating output
        ! self%output = self%activate(matmul(self%weights,x) + self%bias)
        self%output = tanh(matmul(self%weights,self%input) + self%bias)

    end subroutine layer_evaluation

    ! function layer_evaluation(self, x) result (output)
    !     ! defining arguments
    !     class(dense_layer), intent(inout) :: self
    !     real(kind=rkd), dimension(self%input_size), intent(in) :: x
    !     real(kind=rkd), dimension(self%units) :: output
    !
    !     ! adding input to the memory
    !     self%input = x
    !
    !     ! evaluating output
    !     ! self%output = self%activate(matmul(self%weights,x) + self%bias)
    !     self%output = tanh(matmul(self%weights,x) + self%bias)
    !
    ! end function layer_evaluation

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

        ! ! updating weights and biases
        ! self%weights = self%weights - alpha*self%dLdW
        ! self%bias   = self%bias - alpha*self%dLdb

        ! Adam optimization algorithm
        ! steps----------------------------------------------------------------

        ! computing momentum values
        self%mw = beta1*self%mw_1 + (1.0-beta1)*self%dLdW
        self%mb = beta1*self%mb_1 + (1.0-beta1)*self%dLdb
        self%vw = beta2*self%vw_1 + (1.0-beta2)*self%dLdW**2
        self%vb = beta2*self%vb_1 + (1.0-beta2)*self%dLdb**2

        ! ! computing bias corrected momentum variables
        ! self%mw_bar = self%mw/(1.0-beta1)
        ! self%mb_bar = self%mb/(1.0-beta1)
        ! self%vw_bar = self%vw/(1.0-beta2)
        ! self%vb_bar = self%vb/(1.0-beta2)

        ! computing bias corrected momentum variables
        self%mw_bar = self%mw
        self%mb_bar = self%mb
        self%vw_bar = self%vw
        self%vb_bar = self%vb

        ! updating weights and bias with adam optimization algorithm
        self%weights = self%weights - self%mw_bar*alpha/(sqrt(self%vw_bar)+epsilon(beta1))
        self%bias = self%bias - self%mb_bar*alpha/(sqrt(self%vb_bar)+epsilon(beta1))

        ! updating last step of momentum values
        self%mw_1 = self%mw
        self%vw_1 = self%vw
        self%mb_1 = self%mb
        self%vb_1 = self%vb

    end subroutine layer_optimize

end module dense_layer_definitions
