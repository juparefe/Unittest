def check(x):
    discount_20=(x*0.2)
    discount_5=(x*0.05)
    if(x>50000): check=x-discount_20
    else:check=x-discount_5
    return check
