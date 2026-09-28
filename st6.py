print("H0: People do not spend more time on Instagram than YouTube.")
print("H1: People spend more time on Instagram than YouTube.")
from scipy.stats import ttest_ind_from_stats
t_stat, p_value = ttest_ind_from_stats(
    mean1=350,
    std1=50,
    nobs1=30,
    mean2=320,
    std2=50,
    nobs2=30,
    equal_var=True
)
print("t-statistic =", t_stat)
print("p-value =", p_value)
if p_value < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Do not reject the null hypothesis.")
print("Control Group: Users with the old Paytm payment button.")
print("Variant Group: Users with the redesigned payment button.")
print("Metric: Successful payment rate.")
print("H0: The new button does not change the payment rate.")
print("H1: The new button changes the payment rate.")
print("New button clicks = 520")
print("Old button clicks = 480")
print("Difference = 40")
print("The difference alone cannot prove significance.")
print("The p-value helps determine whether the difference may be due to chance.")
print("If p-value is less than 0.05, the difference is statistically significant.")