!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: boundary conditions subroutines definition file
! description:
!    it contains subroutines for defining the boundary conditions
!------------------------------------------------------------------------------

! apply boundary conditions subroutine
! definition-------------------------------------------------------------------
subroutine apply_bc()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! calling bc subroutines for u_field
    call u_bc_north()
    call u_bc_south()
    call u_bc_east()
    call u_bc_west()

    ! calling bc subroutines for v_field
    call v_bc_north()
    call v_bc_south()
    call v_bc_east()
    call v_bc_west()

    ! calling bc subroutines for p_field
    call p_bc_north()
    call p_bc_south()
    call p_bc_east()
    call p_bc_west()

    ! calling bc subroutines for T_field
    call T_bc_north()
    call T_bc_south()
    call T_bc_east()
    call T_bc_west()

    rho = p/R/T

    print *, "updated boundary conditions"

end subroutine apply_bc

! north bc subroutine for
! u_field----------------------------------------------------------------------
subroutine u_bc_north()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (u_north_type == "fixedValue") then
        u(Ny,:) = u_north_value
    elseif (u_north_type == "fixedGradient") then
        u(Ny,:) = u(Ny-1,:) + deltaY*u_north_value
    elseif (u_north_type == "linear") then
        u(Ny,:) = 2.0*u(Ny-1,:) -u(Ny-2,:)
    else
        print *,"unknown bc error for u_north",u_north_type
    end if

end subroutine u_bc_north

! south bc subroutine for
! u_field----------------------------------------------------------------------
subroutine u_bc_south()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (u_south_type == "fixedValue") then
        u(1,:) = u_south_value
    elseif (u_south_type == "fixedGradient") then
        u(1,:) = u(2,:) + deltaY*u_south_value
    elseif (u_south_type == "linear") then
        u(1,:) = 2.0*u(2,:) -u(3,:)
    else
        print *,"unknown bc error for u_south",u_south_type
    end if

end subroutine u_bc_south

! east bc subroutine for
! u_field----------------------------------------------------------------------
subroutine u_bc_east()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (u_east_type == "fixedValue") then
        u(:,Nx) = u_east_value
    elseif (u_east_type == "fixedGradient") then
        u(:,Nx) = u(:,Nx-1) + deltaY*u_east_value
    elseif (u_east_type == "linear") then
        u(:,Nx) = 2.0*u(:,Nx-1) - u(:,Nx-2)
    else
        print *,"unknown bc error for u_east",u_east_type
    end if

end subroutine u_bc_east

! west bc subroutine for
! u_field----------------------------------------------------------------------
subroutine u_bc_west()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (u_west_type == "fixedValue") then
        u(:,1) = u_west_value
    elseif (u_west_type == "fixedGradient") then
        u(:,1) = u(:,2) + deltaY*u_west_value
    elseif (u_west_type == "linear") then
        u(:,1) = 2.0*u(:,2) - u(:,3)
    else
        print *,"unknown bc error for u_west",u_west_type
    end if

end subroutine u_bc_west


! north bc subroutine for
! v_field----------------------------------------------------------------------
subroutine v_bc_north()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (v_north_type == "fixedValue") then
        v(Ny,:) = v_north_value
    elseif (v_north_type == "fixedGradient") then
        v(Ny,:) = v(Ny-1,:) + deltaY*v_north_value
    elseif (v_north_type == "linear") then
        v(Ny,:) = 2.0*v(Ny-1,:) -v(Ny-2,:)
    else
        print *,"unknown bc error for v_north",v_north_type
    end if

end subroutine v_bc_north

! south bc subroutine for
! v_field----------------------------------------------------------------------
subroutine v_bc_south()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (v_south_type == "fixedValue") then
        v(1,:) = v_south_value
    elseif (v_south_type == "fixedGradient") then
        v(1,:) = v(2,:) + deltaY*v_south_value
    elseif (v_south_type == "linear") then
        v(1,:) = 2.0*v(2,:) -v(3,:)
    else
        print *,"unknown bc error for v_south",v_south_type
    end if

end subroutine v_bc_south

! east bc subroutine for
! v_field----------------------------------------------------------------------
subroutine v_bc_east()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (v_east_type == "fixedValue") then
        v(:,Nx) = v_east_value
    elseif (v_east_type == "fixedGradient") then
        v(:,Nx) = v(:,Nx-1) + deltaY*v_east_value
    elseif (v_east_type == "linear") then
        v(:,Nx) = 2.0*v(:,Nx-1) - v(:,Nx-2)
    else
        print *,"unknown bc error for v_east",v_east_type
    end if

end subroutine v_bc_east

! west bc subroutine for
! v_field----------------------------------------------------------------------
subroutine v_bc_west()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (v_west_type == "fixedValue") then
        v(:,1) = v_west_value
    elseif (v_west_type == "fixedGradient") then
        v(:,1) = v(:,2) + deltaY*v_west_value
    elseif (v_west_type == "linear") then
        v(:,1) = 2.0*v(:,2) - v(:,3)
    else
        print *,"unknown bc error for v_west",v_west_type
    end if

end subroutine v_bc_west

! north bc subroutine for
! p_field----------------------------------------------------------------------
subroutine p_bc_north()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (p_north_type == "fixedValue") then
        p(Ny,:) = p_north_value
    elseif (p_north_type == "fixedGradient") then
        p(Ny,:) = p(Ny-1,:) + deltaY*p_north_value
    elseif (p_north_type == "linear") then
        p(Ny,:) = 2.0*p(Ny-1,:) -p(Ny-2,:)
    else
        print *,"unknown bc error for p_north",p_north_type
    end if

end subroutine p_bc_north

! south bc subroutine for
! p_field----------------------------------------------------------------------
subroutine p_bc_south()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (p_south_type == "fixedValue") then
        p(1,:) = p_south_value
    elseif (p_south_type == "fixedGradient") then
        p(1,:) = p(2,:) + deltaY*p_south_value
    elseif (p_south_type == "linear") then
        p(1,:) = 2.0*p(2,:) -p(3,:)
    else
        print *,"unknown bc error for p_south",p_south_type
    end if

end subroutine p_bc_south

! east bc subroutine for
! p_field----------------------------------------------------------------------
subroutine p_bc_east()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (p_east_type == "fixedValue") then
        p(:,Nx) = p_east_value
    elseif (p_east_type == "fixedGradient") then
        p(:,Nx) = p(:,Nx-1) + deltaY*p_east_value
    elseif (p_east_type == "linear") then
        p(:,Nx) = 2.0*p(:,Nx-1) - p(:,Nx-2)
    else
        print *,"unknown bc error for p_east",p_east_type
    end if

end subroutine p_bc_east

! west bc subroutine for
! p_field----------------------------------------------------------------------
subroutine p_bc_west()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (p_west_type == "fixedValue") then
        p(:,1) = p_west_value
    elseif (p_west_type == "fixedGradient") then
        p(:,1) = p(:,2) + deltaY*p_west_value
    elseif (p_west_type == "linear") then
        p(:,1) = 2.0*p(:,2) - p(:,3)
    else
        print *,"unknown bc error for p_west",p_west_type
    end if

end subroutine p_bc_west


! north bc subroutine for
! T_field----------------------------------------------------------------------
subroutine T_bc_north()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (T_north_type == "fixedValue") then
        T(Ny,:) = T_north_value
    elseif (T_north_type == "fixedGradient") then
        T(Ny,:) = T(Ny-1,:) + deltaY*T_north_value
    elseif (T_north_type == "linear") then
        T(Ny,:) = 2.0*T(Ny-1,:) -T(Ny-2,:)
    else
        print *,"unknown bc error for T_north",T_north_type
    end if

end subroutine T_bc_north

! south bc subroutine for
! T_field----------------------------------------------------------------------
subroutine T_bc_south()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (T_south_type == "fixedValue") then
        T(1,:) = T_south_value
    elseif (T_south_type == "fixedGradient") then
        T(1,:) = T(2,:) + deltaY*T_south_value
    elseif (T_south_type == "linear") then
        T(1,:) = 2.0*T(2,:) -T(3,:)
    else
        print *,"unknown bc error for T_south",T_south_type
    end if

end subroutine T_bc_south

! east bc subroutine for
! T_field----------------------------------------------------------------------
subroutine T_bc_east()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (T_east_type == "fixedValue") then
        T(:,Nx) = T_east_value
    elseif (T_east_type == "fixedGradient") then
        T(:,Nx) = T(:,Nx-1) + deltaY*T_east_value
    elseif (T_east_type == "linear") then
        T(:,Nx) = 2.0*T(:,Nx-1) - T(:,Nx-2)
    else
        print *,"unknown bc error for T_east",T_east_type
    end if

end subroutine T_bc_east

! west bc subroutine for
! T_field----------------------------------------------------------------------
subroutine T_bc_west()

    ! importing needed modules
    use modelVars
    use boundary_conditions

    ! overriding automatic variable type assignment
    implicit none

    ! fixedType bc
    if (T_west_type == "fixedValue") then
        T(:,1) = T_west_value
    elseif (T_west_type == "fixedGradient") then
        T(:,1) = T(:,2) + deltaY*T_west_value
    elseif (T_west_type == "linear") then
        T(:,1) = 2.0*T(:,2) - T(:,3)
    else
        print *,"unknown bc error for T_west",T_west_type
    end if

end subroutine T_bc_west

