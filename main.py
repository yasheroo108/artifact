import streamlit as st
import math

st.title("Volume and Surface Area Calculator")

st.markdown("`Made by Yash, Powered by Streamlit`") 
st.markdown("""<a href="https://artifact-inverse.streamlit.app/">Inverse Functions</a>""", unsafe_allow_html=True)

mnmode = st.selectbox("What would you like to calculate?", ("Volume", "Surface Area"))


if mnmode == "Volume":

  mode = st.selectbox("Which 3D shape's volume would you like to calculate?",("Prism", "Pyramid", "Cylinder", "Cone", "Sphere"))

  if mode == "Prism":
      base = st.number_input("Enter the number of sides your prism's base has", min_value=3)

      if base == 3:
          st.latex(r"V = \frac{lwh}{2}")
          st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, H = prism height</p>""", unsafe_allow_html=True)
          length = st.number_input("What is the height of the triangle?", min_value=0.01)
          width = st.number_input("What is the base of the triangle?", min_value=0.01)
          height = st.number_input("What is the height of your prism?", min_value=0.01)
          answer = (float(length) * float(width))/2 * float(height)
          st.write("Your prism's volume is ", answer, " units³.")

      if base == 4:
          
        fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))

        if fourmode == "Trapezoid":
          st.latex(r"V = \frac{(H)(h)(a+b)}{2}")
          st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = base height, a = top side, b = bottom side, H = prism height</p>""", unsafe_allow_html=True)
          a = st.number_input("What is the length of the base's top side (a)?", min_value=0.01)
          b = st.number_input("What is the length of the base's bottom side (b)?", min_value=0.01)
          h = st.number_input("What is the height of the base?", min_value=0.01)
          hp = st.number_input("What is the height of the prism?", min_value=0.01)
          answer = ((h*(a+b))/2)*hp
          st.write("Your prism's volume is ", answer, " units³.")

        if fourmode == "Common":
          st.latex(r"V = lwh")
          st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = length, w = width, h = prism height</p>""", unsafe_allow_html=True)
          length = st.number_input("What is the length of the quadrilateral?", min_value=0.01)
          width = st.number_input("What is the width of the quadrilateral?", min_value=0.01)
          height = st.number_input("What is the height of your prism?", min_value=0.01)
          answer = float(length) * float(width) * float(height)
          st.write("Your prism's volume is ", answer, " units³.")

      if float(base) > 4:
        
        st.warning("Prisms with bases with more than 5 sides will only calculate shapes with regular bases.")
        st.latex(r"V = \frac{APh}{2}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, h = prism height</p>""", unsafe_allow_html=True)
        length = st.number_input("What is the base's side length?", min_value=0.01)
        height = st.number_input("What is the height of your prism?", min_value=0.01)
        answer = (float(length) * float(base) * length / (2 * math.tan(math.radians(180 / base))) * 0.5 *float(height))
        st.write("Your prism's volume is ", answer, " units³.")

  if mode == "Pyramid":
    base = st.number_input("Enter the number of sides that your pyramid's base has base has.", min_value=3)

    if float(base) < 2:
      st.write("Invalid number of sides.")

    if float(base) == 3:
      st.latex(r"V = \frac{lwh}{6}")
      st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = pyramid height</p>""", unsafe_allow_html=True)
      width = st.number_input("What is the base's triangle's base's length?", min_value=0.01)
      length = st.number_input("What is the height of the base's triangle?", min_value=0.01)
      height = st.number_input("What is the height of the pyramid?", min_value=0.01)
      answer = (float(width) * float(length) * 0.5 *float(height) * float(1/3))
      st.write("Your pyramid's volume is ", answer, " units³.")

    if float(base) == 4:

      fourmode = st.selectbox("Do you have a pyramid with a common base or a trapezoid base?", ("Common", "Trapezoid"))
        
      if fourmode == "Common":
        st.latex(r"V = \frac{lwh}{3}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = pyramid height</p>""", unsafe_allow_html=True)
        width = st.number_input("What is the base's width?", min_value=0.01)
        length = st.number_input("What is the height of the base?", min_value=0.01)
        height = st.number_input("What is the height of the pyramid?", min_value=0.01)
        answer = (float(width) * float(length) * float(height) * float(1/3))
        st.write("Your pyramid's volume is ", answer, " units³.")

      if fourmode == "Trapezoid":
        st.latex(r"\frac{(H)(h)(a+b)}{6}")
        st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = base height, a = base top side, b = base bottom side, H = pyramid height</p>""", unsafe_allow_html=True)
        a = st.number_input("What is the base's top length (a)?", min_value=0.01)
        b = st.number_input("What is the base's bottom length (b)?", min_value=0.01)
        h = st.number_input("What is the base's height?", min_value=0.01)
        ph = st.number_input("What is the pyramid's height?", min_value=0.01)
        answer = ((h*(a+b))*ph)/6
        st.write("Your pyramid's volume is ", answer, " units³.")
          
    if float(base) > 4:
      st.warning("Pyramids with bases with more than 5 sides will only calculate shapes with regular bases.")
      st.latex(r"V = \frac{APh}{6}")
      st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, h = pyramid height</p>""", unsafe_allow_html=True)
      length = st.number_input("What is the base's side length?", min_value=0.01)
      height = st.number_input("What is the height of the pyramid?", min_value=0.01)
      answer = (float(length) * float(base) * length / (2 * math.tan(math.radians(180 / base))) * float(0.5) * float(height) * float(1/3))
      st.write("Your pyramid's volume is ", answer, " units³.")

  if mode == "Cylinder":
    circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

    if circlemode == "Radius":
      st.latex(r"V = r^2πh")
      st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = height</p>""", unsafe_allow_html=True)
      radius = st.number_input("What is the radius of the base?", min_value=0.01)
      height = st.number_input("What is the height of the cylinder?", min_value=0.01)
      answer = (float(radius)**2 * math.pi * float(height))
      st.write("Your cylinder's volume is", answer, " units³.")

    if circlemode == "Diameter":
      st.latex(r"V = (\frac{d}{2})^2πh")
      st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = height</p>""", unsafe_allow_html=True)
      diameter = st.number_input("What is the diameter of the circle?", min_value=0.01)
      height = st.number_input("What is the cylinder's height?", min_value=0.01)
      answer = ((float(diameter)/2)**2 * math.pi * float(height))
      st.write("Your cylinder's volume is ", answer, " units³.")

  if mode == "Cone":
      circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

      if circlemode == "Radius":
          st.latex(r"V = \frac{r^2πh}{3}")
          st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = height</p>""", unsafe_allow_html=True)
          radius = st.number_input("What is the radius of the base?", min_value=0.01)
          height = st.number_input("What is the height of the cylinder?", min_value=0.01)
          answer = (math.pi * (float(radius)**2) * (float(height)/3))
          st.write("The volume of the cone is ", answer, " units³.")

      if circlemode == "Diameter":
          st.latex(r"V = \frac{(\frac{d}{2})^2πh}{3}")
          st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = height</p>""", unsafe_allow_html=True)
          diameter = st.number_input("What is the diameter of the base?", min_value=0.01)
          height = st.number_input("What is the height of the cylinder?", min_value=0.01)
          answer = (math.pi * ((float(diameter)/2)**2) * (float(height)/3))
          st.write("The volume of the cone is ", answer, " units³.")


  if mode == "Sphere":
    circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

    if circlemode == "Radius":
      st.latex(r"V = \frac{4}{3}πr^3")
      st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius</p>""", unsafe_allow_html=True)
      radius = st.number_input("What is the radius?", min_value=0.01)
      answer = ((4/3) * math.pi * (float(radius))**3)
      st.write("The volume of the sphere is ", answer, " units³.")

    if circlemode == "Diameter":
      st.latex(r"V = \frac{4}{3}π(\frac{d}{2})^3")
      st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter</p>""", unsafe_allow_html=True)
      diameter = st.number_input("\n\nWhat is the diameter?", min_value=0.01)
      answer = ((4/3) * math.pi * (float(diameter)/2)**3)
      st.write("The volume of the sphere is ", answer, " units³.")







if mnmode == "Surface Area":
    shape = st.selectbox("Which 3D shape's surface area would you like to calculate?",("Prism", "Pyramid", "Cylinder", "Cone", "Sphere"))

    if shape == "Prism":
        base = st.number_input("Enter the number of sides your prism's base has", min_value=3)
        
        if base < 3:
            st.write("Invalid number of sides")

        if base == 3:
            st.latex(r"A = bh+H(b+x+y)")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base, h = height, H = prism height, x = side 2 length, y = side 3 length</p>""", unsafe_allow_html=True)
            blength = st.number_input("What is the length of the base (perpendicular to the height)?", min_value=0.01)
            side2 = st.number_input("What is the length of the second edge of the base?", min_value=0.01)
            side3 = st.number_input("What is the length of the third edge of the base?", min_value=0.01)
            bheight = st.number_input("What is the height of base shape?", min_value=0.01)
            height = st.number_input("What is the height of the prism?", min_value=0.01)
            answer = 2*((blength*bheight)/2) + blength*height + side2*height + side3*height
            st.write("Your prism's SA is ", answer, " units².")

        if base == 4:
            fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))
                
            if fourmode == "Common":
                st.latex(r"A = 2(bh+bH+hH))")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base, h = height, H = prism height</p>""", unsafe_allow_html=True)
                bl = st.number_input("What is the length of the base?", min_value=0.01)
                bw = st.number_input("What is the width of the base?", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                answer = bl*bw + 2*(bl*ph) + 2*(bw*ph)
                st.write("Your answer is ", answer, " units².")

            if fourmode == "Trapezoid":
                st.latex(r"A = h(a+b)+H(a+b+x+y)")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">a = top side, b = bottom side, x = third side, y = fourth side, h = height, H = prism height</p>""", unsafe_allow_html=True)
                a = st.number_input("What is the length of the top side of the base (a)?", min_value=0.01)
                b = st.number_input("What is the length of the bottom side of the base (b)?", min_value=0.01)
                s1 = st.number_input("What is the length of the right/left side of the trapezoid?", min_value=0.01)
                s2 = st.number_input("What is the length of the other side of the trapezoid?", min_value=0.01)
                h = st.number_input("What is the height of the base?", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                answer = 2*((h*(a+b))/2) + a*ph + b*ph + s1*ph + s2*ph
                st.write("Your prism's SA is ", answer, " units².")


        if base > 4:
            st.warning("Prisms with bases with more than 5 sides will only calculate shapes with regular bases.")
            st.latex(r"A = AP+ehs")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, e = edge length, h = prism height, s = no. of sides</p>""", unsafe_allow_html=True)
            e = st.number_input("What is the edge length of the base?", min_value=0.01)
            h = st.number_input("What is the height of the base?", min_value=0.01)
            answer = e*base*(e / (2 * math.tan(math.radians(180 / base)))) + base*(e*h)
            st.write("Your prism's SA is ", answer, " units².")

    
    if shape == "Pyramid":
        base = st.number_input("Enter the number of sides your pyramid's base has", min_value=3)

        if base < 3:
            st.write("Invalid number of sides")


        if base == 3:
            st.latex(r"A = \frac{bh+s(b+x+y)}{2}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base's base, h = base's height, s = slant height, x = second side, y = third side</p>""", unsafe_allow_html=True)
            bw = st.number_input("What is the length of the base (perpendicular to that of the base's height)?", min_value=0.01)
            s2 = st.number_input("What is the length of the second side of the base?", min_value=0.01)
            s3 = st.number_input("What is the length of the third side of the base?", min_value=0.01)
            bh = st.number_input("What is the height of the base?", min_value=0.01)
            sl = st.number_input("What is the slant height of each of the non-base triangles?", min_value=0.01)
            answer = (bw*bh)/2 + (bw*sl)/2 + (s2*sl)/2 + (s3*sl)/2
            st.write("Your pyramid's SA is ", answer, " units².")

        if base == 4:

            fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))
                    
            if fourmode == "Common":
                st.latex(r"A = bh+s(b+h)")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base, h = height, s = slant</p>""", unsafe_allow_html=True)
                bl = st.number_input("What is the length of the base?", min_value=0.01)
                bw = st.number_input("What is the width of the base?", min_value=0.01)
                sl = st.number_input("What is the slant length of the prism?", min_value=0.01)
                answer = bl*bw + 2*(bl*sl)/2 + 2*(bw*sl)/2
                st.write("Your pyramid's SA is ", answer, " units².")

            if fourmode == "Trapezoid":
                st.latex(r"A = \frac{s(a+b+x+y)+h(a+b)}{2}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = height, a = base top side, b = base bottom side, x = third side, y = fourth side, s = slant</p>""", unsafe_allow_html=True)
                a = st.number_input("What is the length of the top side of the base (a)?", min_value=0.01)
                b = st.number_input("What is the length of the bottom side of the base (b)?", min_value=0.01)
                s1 = st.number_input("What is the length of the right/left side of the trapezoid?", min_value=0.01)
                s2 = st.number_input("What is the length of the other side of the trapezoid?", min_value=0.01)
                h = st.number_input("What is the height of the base?", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                answer = 2*((h*(a*b))/2) + a*ph + b*ph + s1*ph + s2*ph
                st.write("Your prism's SA is ", answer, " units².")

        if base > 4:
            st.warning("Pyramids with bases with more than 5 sides will only calculate shapes with regular bases.")
            st.latex(r"A = \frac{AP+esx}{2}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, x = no. of sides, e = edge length, s = slant</p>""", unsafe_allow_html=True)
            e = st.number_input("What is the length of an edge of the base?", min_value=0.01)
            sl = st.number_input("What is the slant height?", min_value=0.01)
            answer = e*base*(e / (2 * math.tan(math.radians(180 / base))))*0.5 + base*(e*sl)/2
            st.write("Your prism's SA is ", answer, " units².")

    if shape == "Cylinder":
        circmode = st.selectbox("Do you have the radius or diameter?", ("Radius", "Diameter"))
        
        if circmode == "Radius":
            st.latex(r"A = πr²+Ch")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, C = circumference, h = prism height</p>""", unsafe_allow_html=True)           
            r = st.number_input("What is the length of the radius?", min_value=0.01)
            h = st.number_input("What is the height of the prism?", min_value=0.01)
            answer = (2*r*math.pi)*h + 2*(r**2*math.pi)
            st.write("Your cylinder's SA is ", answer, " units².")


        if circmode == "Diameter":
            st.latex(r"A = π(\frac{d}{2})²+Ch")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, C = circumference, h = prism height</p>""", unsafe_allow_html=True)
            d = st.number_input("What is the length of the diameter?", min_value=0.01)
            h = st.number_input("What is the height of the prism?", min_value=0.01)
            answer = d*math.pi*h + 2*((d/2)**2*math.pi)
            st.write("Your cylinder's SA is ", answer, " units².")

    if shape == "Cone":
        circmode = st.selectbox("Do you have the radius or diameter?", ("Radius", "Diameter"))
        
        if circmode == "Radius":
            st.latex(r"A = πr(r+\sqrt{h²+r²})")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = prism height</p>""", unsafe_allow_html=True)
            r = st.number_input("What is the length of the radius?", min_value=0.01)
            h = st.number_input("What is the height of the prism?", min_value=0.01)
            answer = math.pi*r*(r+math.sqrt(h**2+r**2))
            st.write("Your cone's SA is ", answer, " units².")


        if circmode == "Diameter":
            st.latex(r"A = π\frac{d}{2}(\frac{d}{2}+\sqrt{h²+(\frac{d}{2})²})")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = prism height</p>""", unsafe_allow_html=True)
            d = st.number_input("What is the length of the diameter?", min_value=0.01)
            h = st.number_input("What is the height of the prism?", min_value=0.01)
            answer = math.pi*(d/2)*((d/2)+math.sqrt(h**2+(d/2)**2))
            st.write("Your cone's SA is ", answer, " units².")
    
    if shape == "Sphere":
        circmode = st.selectbox("Do you have the radius or diameter?", ("Radius", "Diameter"))
        
        if circmode == "Radius":
            st.latex(r"A = 4πr²")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius</p>""", unsafe_allow_html=True)
            r = st.number_input("What is the length of the radius?", min_value=0.01)
            answer = math.pi*4*r**2
            st.write("Your sphere's SA is ", answer, " units².")


        if circmode == "Diameter":
            st.latex(r"A = 4π(\frac{d}{2})²")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter</p>""", unsafe_allow_html=True)
            d = st.number_input("What is the length of the diameter?", min_value=0.01)
            answer = math.pi*4*(d/2)**2
            st.write("Your sphere's SA is ", answer, " units².")
    

