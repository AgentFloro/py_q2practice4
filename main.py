from pyscript import display, document

def add_brand(e):
    document.getElementById('output1').innerHTML = ""

    brands = {"uniqlo", "Bench",  "Levis"}

    input_brand = document.getElementById('input1').value

    new_brand_set = {input_brand}

    All_brands = brands | new_brand_set

    total_brands =len(brands | new_brand_set)

    brand_list = "<br>".join(sorted(All_brands))

    document.getElementById('output1').innerHTML = (f"All brands: <br>{brand_list}")
    display(f'total brands: {total_brands}', target= "output1" )
