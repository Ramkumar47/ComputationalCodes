!------------------------------------------------------------------------------
! Particle Swarm Optimization
! model variables definition
!------------------------------------------------------------------------------

module modelVariables

    use parameters

    implicit none

    ! defining scalars
    real(kind=rkd) :: f_value, f_gbest

    ! defining particle arrays
    real(kind=rkd), dimension(Np,Nd) :: x,v,r1,r2,x_np1,v_np1,Pbest
    real(kind=ikd), dimension(Nd) :: Gbest
    real(kind=ikd), dimension(Np) :: f_eval,f_pbest

end module modelVariables
