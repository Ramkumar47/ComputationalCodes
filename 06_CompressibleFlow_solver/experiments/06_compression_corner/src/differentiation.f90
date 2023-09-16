!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: differentiation computation file
! description:
!    it contains subroutines related to differentiation based on inverse
!    grid transformation
!------------------------------------------------------------------------------

! module definition for common differentiation
! variables--------------------------------------------------------------------
module differentiation

    ! importing needed modules
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! defining common differentiation variables
    real(kind=rkd), dimension(Ny,Nx) :: field, dField_dEps, dField_dEta

end module differentiation

! subroutine for ddx computation-----------------------------------------------
subroutine compute_ddx(input_field, method, ddx_field)

    ! importing needed modules
    use differentiation

    ! overriding automatic variable type assignment
    implicit none

    ! defining local variables
    real(kind=rkd), dimension(Ny,Nx), intent(in) :: input_field
    real(kind=rkd), dimension(Ny,Nx), intent(out) :: ddx_field
    character(len=*), intent(in) :: method

    ! assigning input field values
    field = input_field

    ! calling respective the method of discretization
    if (trim(method) == "forward") then
        call dd_forward()
    elseif (method == "backward") then
        call dd_backward()
    elseif (method == "central") then
        call dd_central()
    else
        print *,"Uknown method of discretization ! : ", method
        ERROR stop
    endif

    ! computing ddx of given input field
    ddx_field = 1.0/Jac*(dField_dEps*dYdEta - dField_dEta*dYdEps)

end subroutine compute_ddx

! subroutine for ddy computation-----------------------------------------------
subroutine compute_ddy(input_field, method, ddy_field)

    ! importing needed modules
    use differentiation

    ! overriding automatic variable type assignment
    implicit none

    ! defining local variables
    real(kind=rkd), dimension(Ny,Nx), intent(in) :: input_field
    real(kind=rkd), dimension(Ny,Nx), intent(out) :: ddy_field
    character(len=*), intent(in) :: method

    ! assigning input field values
    field = input_field

    ! calling respective the method of discretization
    if (trim(method) == "forward") then
        call dd_forward()
    elseif (method == "backward") then
        call dd_backward()
    elseif (method == "central") then
        call dd_central()
    else
        print *,"Uknown method of discretization ! : ", method
        ERROR stop
    endif

    ! computing ddy of given input field
    ddy_field = 1.0/Jac*(dField_dEta*dXdEps - dField_dEps*dXdEta)

end subroutine compute_ddy


! subroutine to compute dd_forward in computation field
! domain-----------------------------------------------------------------------
subroutine dd_forward()

    ! importing needed modules
    use differentiation

    ! computing ddEps of given field
    do i = 1,Nx-1
        dField_dEps(:,i) = (field(:,i+1)-field(:,i))/dEps
    end do
    dField_dEps(:,Nx) = (field(:,Nx) - field(:,Nx-1))/dEps

    ! computing ddEta of given field
    do j = 1,Ny-1
        dField_dEta(j,:) = (field(j+1,:) - field(j,:))/dEta
    end do
    dField_dEta(Ny,:) = (field(Ny,:) - field(Ny-1,:))/dEta

end subroutine dd_forward

! subroutine to compute dd_backward in computation field
! domain-----------------------------------------------------------------------
subroutine dd_backward()

    ! importing needed modules
    use differentiation

    ! computing ddEps of given field
    do i = 2,Nx
        dField_dEps(:,i) = (field(:,i)-field(:,i-1))/dEps
    end do
    dField_dEps(:,1) = (field(:,2) - field(:,1))/dEps

    ! computing ddEta of given field
    do j = 2,Ny
        dField_dEta(j,:) = (field(j,:) - field(j-1,:))/dEta
    end do
    dField_dEta(1,:) = (field(2,:) - field(1,:))/dEta


end subroutine dd_backward

! subroutine to compute dd_central in computation field
! domain-----------------------------------------------------------------------
subroutine dd_central()

    ! importing needed modules
    use differentiation

    ! computing ddEps of given field
    do i = 2,Nx-1
        dField_dEps(:,i) = (field(:,i+1)-field(:,i-1))/dEps/2.0
    end do
    dField_dEps(:,1) = (field(:,2) - field(:,1))/dEps
    dField_dEps(:,Nx) = (field(:,Nx) - field(:,Nx-1))/dEps

    ! computing ddEta of given field
    do j = 2,Ny-1
        dField_dEta(j,:) = (field(j+1,:) - field(j-1,:))/dEta/2.0
    end do
    dField_dEta(1,:) = (field(2,:) - field(1,:))/dEta
    dField_dEta(Ny,:) = (field(Ny,:) - field(Ny-1,:))/dEta

end subroutine dd_central
