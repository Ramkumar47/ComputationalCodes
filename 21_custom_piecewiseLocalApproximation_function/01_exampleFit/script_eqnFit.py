#!/bin/python3
"""----------------------------------------------------------------------------
Curvefit trial for the Blasius solution variables
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from localApproximation import cubic_fit


# reading blasius solution data
fid = pd.read_csv("BL_solutionData.csv")

N = fid.shape[0]
eta = fid["eta"].to_numpy()
f = fid["f"].to_numpy()
f_dash = fid["f_dash"].to_numpy()

# approximating f profile------------------------------------------------------
# creating knot indices
knots_location = [0,2,6,eta[-1]]

coeffs, f_hat, R2, knot_indices = cubic_fit(eta,f,knots_location)
coeffs["knot_start_value"] = knots_location[:-1]
coeffs.to_csv("f_approx_coeffs.csv", index = None)

plt.figure()
plt.plot(f_hat,eta,'-b', label = "approximated")
plt.plot(f,eta,'-r', label = "actual")
plt.plot(f[knot_indices], eta[knot_indices], 'ok', label = "knots")
plt.legend()
plt.grid()
plt.xlabel("f")
plt.ylabel("eta")
plt.title(" R-squared = "+str(np.round(R2,6)))
plt.savefig("f_approx.png", dpi = 150)

#  plt.show()

# approximating f_dash profile-------------------------------------------------
# creating knot indices
knots_location = [0,3,4,5,6,7,8,eta[-1]]

coeffs, f_dash_hat, R2, knot_indices = cubic_fit(eta,f_dash,knots_location)
coeffs["knot_start_value"] = knots_location[:-1]
coeffs.to_csv("f_dash_approx_coeffs.csv", index = None)

plt.figure()
plt.plot(f_dash_hat,eta,'-b', label = "approximated")
plt.plot(f_dash,eta,'-r', label = "actual")
plt.plot(f_dash[knot_indices], eta[knot_indices],'ok', label = "knots")
plt.legend()
plt.grid()
plt.xlabel("f_dash")
plt.ylabel("eta")
plt.title(" R-squared = "+str(np.round(R2,6)))
plt.savefig("f_dash_approx.png", dpi = 150)

plt.show()
