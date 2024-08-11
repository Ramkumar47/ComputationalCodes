!------------------------------------------------------------------------------
! single composed neurons curve fit program : input parameters definition
!------------------------------------------------------------------------------

module parameters

    implicit none

    ! defining standard datatypes
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! size of dataset
    integer(kind=ikd), parameter :: N_size = 101

    ! neuron count incluing output and excluding input
    integer(kind=ikd), parameter :: N_neuron = 6

    ! number of epochs
    integer(kind=ikd), parameter :: N_epochs = 100000

    ! learning rate
    real(kind=rkd), parameter :: beta = 1.0

    ! load weights ?
    logical, parameter :: load_weights = .false.

end module parameters
