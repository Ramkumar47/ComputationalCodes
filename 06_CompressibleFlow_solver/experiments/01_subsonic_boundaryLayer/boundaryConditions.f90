!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: boundary conditions definition file
! description:
!    it contains module for defining boundary conditions
!------------------------------------------------------------------------------

! boundary conditions module definition
module boundary_conditions

    ! importing needed modules
    use parameters

    ! overriding automatic variable type assignment
    implicit none

    ! general bc types---------------------------------------------------------
    ! 1) "fixedValue" - dirichlet bc, requires a value to be specified
    ! 2) "fixedGradient" - neumann bc, requires a value to be specified
    ! 3) "linear" - linear extrapolation, does not require any value
    !--------------------------------------------------------------------------

    ! boundary regions specification-------------------------------------------
    ! 1) "north" - Y+ side
    ! 2) "south" - Y- side
    ! 3) "east"  - X+ side
    ! 4) "west"  - X- side
    !--------------------------------------------------------------------------

    ! bcs for "u" field
    ! variable-----------------------------------------------------------------
    ! north
    character(len=30), parameter :: u_north_type = "fixedValue"
    real(kind=ikd), parameter :: u_north_value = M_inf*sqrt(g*R*T_inf)
    ! south
    character(len=30), parameter :: u_south_type = "fixedValue"
    real(kind=ikd), parameter :: u_south_value = 0.0
    ! east
    character(len=30), parameter :: u_east_type = "fixedGradient"
    real(kind=ikd), parameter :: u_east_value = 0.0
    ! west
    character(len=30), parameter :: u_west_type = "fixedValue"
    real(kind=ikd), parameter :: u_west_value = M_inf*sqrt(g*R*T_inf)

    ! bcs for "v" field
    ! variable-----------------------------------------------------------------
    ! north
    character(len=30), parameter :: v_north_type = "fixedValue"
    real(kind=ikd), parameter :: v_north_value = 0.0
    ! south
    character(len=30), parameter :: v_south_type = "fixedValue"
    real(kind=ikd), parameter :: v_south_value = 0.0
    ! east
    character(len=30), parameter :: v_east_type = "linear"
    real(kind=ikd), parameter :: v_east_value = 0.0
    ! west
    character(len=30), parameter :: v_west_type = "fixedValue"
    real(kind=ikd), parameter :: v_west_value = 0.0

    ! bcs for "p" field
    ! variable-----------------------------------------------------------------
    ! north
    character(len=30), parameter :: p_north_type = "fixedValue"
    real(kind=ikd), parameter :: p_north_value = P_inf
    ! south
    character(len=30), parameter :: p_south_type = "linear"
    real(kind=ikd), parameter :: p_south_value = P_inf
    ! east
    character(len=30), parameter :: p_east_type = "fixed"
    real(kind=ikd), parameter :: p_east_value = P_inf
    ! west
    character(len=30), parameter :: p_west_type = "linear"
    real(kind=ikd), parameter :: p_west_value = 0.0

    ! bcs for "T" field
    ! variable-----------------------------------------------------------------
    ! north
    character(len=30), parameter :: T_north_type = "fixedValue"
    real(kind=ikd), parameter :: T_north_value = T_inf
    ! south
    character(len=30), parameter :: T_south_type = "fixedValue"
    real(kind=ikd), parameter :: T_south_value = T_inf
    ! east
    character(len=30), parameter :: T_east_type = "linear"
    real(kind=ikd), parameter :: T_east_value = 0.0
    ! west
    character(len=30), parameter :: T_west_type = "fixedValue"
    real(kind=ikd), parameter :: T_west_value = T_inf

end module boundary_conditions

