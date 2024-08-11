!------------------------------------------------------------------------------
! single composed neurons curve fit program : model variables definition
!------------------------------------------------------------------------------

module variables

    use parameters
    use dense_layer_definitions

    implicit none

    ! defining integer scalar variables
    integer(kind=ikd) :: ival,i,j,epoch

    ! defining real scalar variables
    real(kind=rkd) :: dLdz,dLdw,dLdb

    ! defining character variables
    character(len=50) :: dummy_name

    ! defining integer array variables

    ! defining real array variables
    ! real(kind=rkd), dimension(N_size) :: x,y,y_pred
    real(kind=rkd), dimension(N_data) :: x,y,y_pred
    real(kind=rkd), dimension(:),allocatable :: tmp1,tmp2
    real(kind=rkd), dimension(layers(N_layer)) :: dLdsigma,lossVal

    ! defining dense layer array variable
    type(dense_layer), dimension(N_layer) :: dense_layer_array

end module variables
