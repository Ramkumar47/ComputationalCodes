!------------------------------------------------------------------------------
! single composed neurons curve fit program : model variables definition
!------------------------------------------------------------------------------

module variables

    use parameters
    use neuron_definitions

    implicit none

    ! defining integer scalar variables
    integer(kind=ikd) :: ival,i,j,epoch

    ! defining real scalar variables
    real(kind=rkd) :: lossVal,tmp,dLdz,dLdw,dLdb

    ! defining character variables
    character(len=50) :: dummy_name

    ! defining integer array variables

    ! defining real array variables
    real(kind=rkd), dimension(N_size) :: x,y,y_pred

    ! defining neuron array variables
    type(neuron), dimension(N_neuron) :: neuron_array

end module variables
