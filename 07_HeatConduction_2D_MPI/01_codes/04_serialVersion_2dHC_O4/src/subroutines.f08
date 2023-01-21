!------------------------------------------------------------------------------!
! 2D Heat conduction solver using 4th order accurate Central diff. scheme      !
! Serial version code                                                          !
!                                                                              !
! subroutines definitions                                                      !
!------------------------------------------------------------------------------!

! initializer subroutine
! definition-------------------------------------------------------------------
subroutine initializer()

    use modelVariables

    implicit none

    ! generating grid
    X = 0.0
    Y = 0.0
    do i = 1,Nxg
        do j = 1,Nyg
            X(j,i) = float(i-2)*dx
            Y(j,i) = float(j-2)*dy
        end do
    end do

    ! initializing temperature field
    T = 0.25*(T_east+T_west+T_north+T_south)
    T(:,1:2) = T_west
    T(1:2,:) = T_south
    T(Nyg-1:Nyg,:) = T_north
    T(:,Nxg-1:Nxg) = T_east

    T_old = T

    print *,"initialization done"

end subroutine initializer

! update ghostnodes subroutine
! definition-------------------------------------------------------------------
subroutine update_ghostNodes()

    use modelVariables

    implicit none

    ! linear extrapolation
    T(:,1) = 2.0*T(:,2) - T(:,3)
    T(:,Nxg) = 2.0*T(:,Nxg-1) - T(:,Nxg-2)
    T(1,:) = 2.0*T(2,:) - T(3,:)
    T(Nyg,:) = 2.0*T(Nyg-1,:) - T(Nyg-2,:)

    print *,"ghost nodes updated"

end subroutine update_ghostNodes

! write_csv subroutine
! definition-------------------------------------------------------------------
subroutine write_csv()

    use modelVariables

    implicit none

    open(unit = 1, file = "output_data.csv")

    write(unit=1, fmt=*) "X,Y,Z,T"

    50 format(ES12.5,",",ES12.5,","ES12.5,","ES12.5)

    do i = 1+Ng,Nxg-Ng
        do j = 1+Ng,Nyg-Ng
            write(unit = 1, fmt=50) X(j,i),Y(j,i),0.0,T(j,i)
        end do
    end do

    print *,"csv file written"

end subroutine write_csv
