"""
RECORD CHECK  -  my version
===========================

Name  :  Neema Rutikanga
Lane  :  Cyber     
Date  :  September 30, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#label= input("Label: ")
#first = float(input("First: "))
#second = float(input("Second: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

#difference = first - second
#percent = (first / second) * 100 
#print(input("Difference:", difference))
#print(input("Percent:", percent))

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

label1= "10.0.0.5"
label2 =   12.0
label3 = 400.0
print("=" * 34)
print(f"  Source IP  -  {label1}")
print("=" * 34)
print("failed_logins: ",  f"{label2:>10.2f}")
print("total_attempts: ", f"{label3:>10.2f}")
print("=" * 34)
# : your report lines go here




# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
