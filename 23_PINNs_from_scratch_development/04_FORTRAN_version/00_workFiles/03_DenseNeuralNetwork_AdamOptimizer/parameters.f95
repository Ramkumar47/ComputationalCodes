!------------------------------------------------------------------------------
! single composed neurons curve fit program : input parameters definition
!------------------------------------------------------------------------------

module parameters

    implicit none

    ! defining standard datatypes
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! dense layer units count including output and excluding input
    integer(kind=ikd), parameter :: input_size = 1
    integer(kind=ikd), dimension(*), parameter :: layers = (/1/)
    integer(kind=ikd), parameter :: N_layer = size(layers)

    ! number of epochs
    integer(kind=ikd), parameter :: N_epochs = 100000

    ! learning rate
    real(kind=rkd), parameter :: alpha = 1e-3

    ! load and  weights
    logical, parameter :: load_weights = .false.
    logical, parameter :: save_weights = .true.

    ! data file name and size
    ! character(len=50),parameter :: datafile_name = "normalized_data.txt"
    ! integer(kind=ikd),parameter :: N_data = 7501
    ! integer(kind=ikd),parameter :: N_data = 101
    character(len=50),parameter :: datafile_name = "normalized_data.csv"
    integer(kind=ikd),parameter :: N_data = 740

    ! parameters related to adam optimizer
    real(kind=rkd),parameter :: beta1 = 0.9, beta2 = 0.9

end module parameters