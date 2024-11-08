import streamlit as st
import math

#add that is answer is negative its impossible

st.title("Reverse Functions")

st.markdown("`Made by Yash, Powered by Streamlit`") 
st.markdown("""<a href="https://testytester.streamlit.app/">Surface Area and Volume</a>""", unsafe_allow_html=True)

mnmode = st.selectbox("Would you like to reverse volume or surface area?", ("Volume", "Surface Area"))

if mnmode == "Volume":
    mode = st.selectbox("Which 3D shape's variable would you like to calculate", ("Prism", "Pyramid", "Cylinder", "Cone", "Sphere"))

    if mode == "Prism":
        base = st.number_input("How many sides does your prism's base have?", min_value=3)
        
        if base == 3:
            st.latex(r"V = \frac{lwh}{2}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = prism height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Length", "Width", "Prism Height"))

            if var == "Length":
                st.latex(r"l = \frac{2V}{wh}")
                w = st.number_input("What is the base's width?", min_value=0.01)
                h = st.number_input("What is the prism's height?", min_value=0.01)
                v = st.number_input("What is the prism's volume?", min_value=0.01)
                answer = ((v/h)/w)*2
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The length of the base is ", answer, " units.")

            if var == "Width":
                st.latex(r"w = \frac{2V}{lh}")
                l = st.number_input("What is the base's length?", min_value=0.01)
                h = st.number_input("What is the prism's height?", min_value=0.01)
                v = st.number_input("What is the prism's volume?", min_value=0.01)
                answer = ((v/h)/l)*2
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The width of the base is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"h = \frac{2V}{lw}")
                w = st.number_input("What is the base's width?", min_value=0.01)
                l = st.number_input("What is the base length?", min_value=0.01)
                v = st.number_input("What is the prism's volume?", min_value=0.01)
                answer = ((v/l)/w)*2
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The height of the prism is ", answer, " units.")

        if base == 4: 
            fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))

            if fourmode == "Common":
                st.latex(r"V = lwh")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = length, w = width, h = prism height</p>""", unsafe_allow_html=True)
                var = st.selectbox("Which variable would you like to calculate?", ("Length", "Width", "Prism Height"))
                if var == "Length":
                    st.latex(r"l = \frac{V}{wh}")
                    w = st.number_input("What is the width of the base?", min_value=0.01)
                    h = st.number_input("What is the height of the prism?", min_value=0.01)
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    answer = (v/w)/h
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The length is ", answer, " units.")

                if var == "Width":
                    st.latex(r"w = \frac{V}{lh}")
                    l = st.number_input("What is the length of the base?", min_value=0.01)
                    h = st.number_input("What is the height of the prism?", min_value=0.01)
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    answer = (v/l)/h
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The width is ", answer, " units.")

                if var == "Prism Height":
                    st.latex(r"h = \frac{V}{lw}")
                    l = st.number_input("What is the length of the base?", min_value=0.01)
                    w = st.number_input("What is the width of the base?", min_value=0.01)
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    answer = (v/l)/w
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:   
                        st.write("The height is ", answer, " units.")

            if fourmode == "Trapezoid":
                st.latex(r"V = \frac{(H)(h)(a+b)}{2}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = base height, a = top side, b = bottom side, H = prism height</p>""", unsafe_allow_html=True)
                var = st.selectbox("Which variable would you like to calculate?", ("a", "b", "Base Height", "Prism Height"))

                if var == "a":
                    st.latex(r"a = \frac{2V}{Hh}-b")
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    bh = st.number_input("What is the height of the base?", min_value=0.01)
                    ph = st.number_input("What is the height of the prism?", min_value=0.01)
                    b = st.number_input("What is b (top or bottom side of base)?", min_value=0.01)
                    answer = (((2*v)/ph)/bh)-b
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("a is ", answer, " units.")

                if var == "b":
                    st.latex(r"b = \frac{2V}{Hh}-a")
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    bh = st.number_input("What is the height of the base?", min_value=0.01)
                    ph = st.number_input("What is the height of the prism?", min_value=0.01)
                    a = st.number_input("What is a (top or bottom side of base)?", min_value=0.01)
                    answer = (((2*v)/ph)/bh)-a
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("b is ", answer, " units.")

                if var == "Base Height":
                    st.latex(r"h = \frac{2V}{H(a+b)}")
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    ph = st.number_input("What is the prism's height?", min_value=0.01)
                    a = st.number_input("What is a (top or bottom side of base)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    answer = ((2*v)/ph)/(a+b)
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The base height is ", answer, " units.")

                if var == "Prism Height":
                    st.latex(r"H = \frac{2V}{h(a+b)}")
                    v = st.number_input("What is the volume of the prism?", min_value=0.01)
                    bh = st.number_input("What is the base height?", min_value=0.01)
                    a = st.number_input("What is a (top or bottom side)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    answer = (2*v)/(bh*(a+b))
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The prism height is ", answer, " units")

        if base > 4:
            st.warning("Prisms with bases with more than 5 sides will only calculate shapes with regular bases.")
            st.latex(r"V = \frac{APh}{2}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, h = prism height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Apothem", "Perimeter", "Prism Height"))

            if var == "Apothem":
                st.latex(r"A = \frac{\frac{P}{x}}{2tan(\frac{180}{x})}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
                p = st.number_input("What is the perimieter of the base?", min_value=0.01)
                answer = (p/base)/(2*math.tan(math.radians(180/base)))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The apothem is ", answer, " units.")

            if var == "Perimeter":
                st.latex(r"P = Ax(2tan(\frac{180}{x}))")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
                a = st.number_input("What is the apothem of the base?", min_value=0.01)
                answer = a*(2*math.tan(math.radians(180/base)))*base
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The perimieter is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"h = \frac{2V}{AP}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                e = st.number_input("What is the edge length of the base?", min_value=0.01)
                answer = (2*v) / ((e / (2*math.tan(math.radians(180 / base)))) * e*base)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The prism height is ", answer, " units.")

    if mode == "Pyramid":
        base = st.number_input("How many sides does your pyramid's base have?", min_value=3)

        if base == 3:
            st.latex(r"V = \frac{lwh}{6}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = pyramid height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Base Length", "Base Width", "Pyramid Height"))

            if var == "Base Length":
                st.latex(r"l = \frac{6V}{wh}")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                w = st.number_input("What is the width of the base?", min_value=0.01)
                h = st.number_input("What is the height of the pyramid?", min_value=0.01)
                answer = (6*v)/(w*h)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The base's length is ", answer, " units.")

            if var == "Base Width":
                st.latex(r"w = \frac{6V}{lh}")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                l = st.number_input("What is the length of the base?", min_value=0.01)
                h = st.number_input("What is the height of the pyramid?", min_value=0.01)
                answer = (6*v)/(l*h)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The base's width is ", answer, " units.")

            if var == "Pyramid Height":
                st.latex(r"h = \frac{6V}{lw}")
                v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                l = st.number_input("What is the length of the base?", min_value=0.01)
                w = st.number_input("What is the width of the base?", min_value=0.01)
                answer = (6*v)/(l*w)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The pyramid's height is ", answer, " units.")

        if base == 4:
            fourmode = st.selectbox("Do you have a pyramid with a common base or a trapezoid base?", ("Common", "Trapezoid"))

            if fourmode == "Common":
                st.latex(r"V = \frac{lwh}{3}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">l = base length, w = base width, h = base height</p>""", unsafe_allow_html=True)
                var = st.selectbox("Which variable would you like to calculate?", ("Base Length", "Base Width", "Pyramid Height"))
                if var == "Base Length":
                    st.latex(r"l = \frac{3V}{hw}")
                    v = st.number_input("What is the volume of your pyramid?", min_value=0.01)
                    bw = st.number_input("What is the base width?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    answer = (3*v)/(ph*bw)
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The length is ", answer, " units.")

                if var == "Base Width":
                    st.latex(r"w = \frac{3V}{lh}")
                    v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                    l = st.number_input("What is the length of the base?", min_value=0.01)
                    h = st.number_input("What is the height of the prism?", min_value=0.01)
                    answer = (3*v)/(l*h)
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The width of the base is ", answer, " units.")

                if var == "Pyramid Height":
                    st.latex(r"h = \frac{3V}{lw}")
                    v = st.number_input("What is the volume?", min_value=0.01)
                    l = st.number_input("What is the length of the base?", min_value=0.01)
                    w = st.number_input("What is the width of the base?", min_value=0.01)
                    answer = (3*v)/(l*w)
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The pyramid height is ", answer, " units.")
            
            if fourmode == "Trapezoid":
                st.latex(r"\frac{(H)(h)(a+b)}{6}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = base height, a = base top side, b = base bottom side, H = prism height</p>""", unsafe_allow_html=True)
                var = st.selectbox("What variable would you like to calculate?", ("Base Height", "a", "b", "Prism Height"))
                if var == "Base Height":
                    st.latex(r"h = \frac{6V}{H(a+b)}")
                    v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                    ph = st.number_input("What is the pyramid height?", min_value=0.01)
                    a = st.number_input("What is a of the base (The top of bottoms side of the trapezoid)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    answer = (6*v)/(ph*(a+b))
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The base height is ", answer, " units.")

                if var == "a":
                    st.latex(r"a = \frac{6V}{Hh}-b")
                    v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                    ph = st.number_input("What is the height of the pyramid?", min_value=0.01)
                    bh = st.number_input("What is the height of the base?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    answer = ((6*v)/(ph*bh))-b
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("a is", answer, " units.")

                if var == "b":
                    st.latex(r"b = \frac{6V}{Hh}-a")
                    v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                    ph = st.number_input("What is the height of the pyramid?", min_value=0.01)
                    bh = st.number_input("What is the height of the base?", min_value=0.01)
                    a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                    answer = ((6*v)/(ph*bh))-a
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("b is", answer, " units.")
                
                if var == "Prism Height":
                    st.latex(r"H = \frac{6V}{h(a+b)}")
                    v = st.number_input("What is the volume of the pyramid?", min_value=0.01)
                    bh = st.number_input("What is the base pyramid?", min_value=0.01)
                    a = st.number_input("What is a of the base (The top of bottoms side of the trapezoid)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    answer = (6*v)/(bh*(a+b))
                    if answer < 0:
                        st.write("Invalid circumstances.")
                    else:
                        st.write("The pyramid height is ", answer, " units.")

        if base > 4:
            st.warning("Pyramids with bases with more than 5 sides will only calculate shapes with regular bases.")
            st.latex(r"V = \frac{APh}{6}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, h = pyramid height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Apothem", "Perimeter", "Pyramid Height"))

            if var == "Apothem":
                st.latex(r"A = \frac{\frac{P}{x}}{2tan(\frac{180}{x})}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
                p = st.number_input("What is the perimieter of the base?", min_value=0.01)
                answer = (p/base)/(2*math.tan(math.radians(180/base)))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The apothem is ", answer, " units.")

            if var == "Perimeter":
                st.latex(r"P = Ax(2tan(\frac{180}{x}))")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides of base</p>""", unsafe_allow_html=True)
                a = st.number_input("What is the apothem of the base?", min_value=0.01)
                answer = a*(2*math.tan(math.radians(180/base)))*base
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The perimieter is ", answer, " units.")

            if var == "Pyramid Height":
                st.latex(r"h = \frac{6V}{AP}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                e = st.number_input("What is the side length of the base?", min_value=0.01)
                answer = (6*v)/((e / (2 * math.tan(math.radians(180 / base))))*(e*base))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The pyramid height is ", answer, " units.")

    if mode == "Cylinder":
        circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

        if circlemode == "Radius":
            st.latex(r"V = r^2πh")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = height</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Radius", "Cylinder Height"))

            if var == "Radius":
                st.latex(r"r = \sqrt{\frac{V}{πh}}")
                v = st.number_input("What is the volume of the cylinder?", min_value=0.01)
                h = st.number_input("What is the height of the cylinder?", min_value=0.01)
                answer = math.sqrt(v/(math.pi*h))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The radius is ", answer, " units.")

            if var == "Cylinder Height":
                st.latex(r"h = \frac{V}{πr²}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                r = st.number_input("What is the radius?", min_value=0.01)
                answer = v/(math.pi*r**2)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The cylinder height is ", answer, " units.")
                

        if circlemode == "Diameter":
            st.latex(r"V = (\frac{d}{2})^2πh")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = height</p>""", unsafe_allow_html=True)
            var = st.selectbox("What is the variable you'd like to calculate?", ("Diameter", "Prism Height"))

            if var == "Diameter":
                st.latex(r"d = 2\sqrt{\frac{V}{πh}}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                h = st.number_input("What is the height of the prism?", min_value=0.01)
                answer = 2*(math.sqrt((v/(math.pi*h))))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The diameter is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"h = \frac{V}{π(\frac{d}{2})²}")
                v = st.number_input("What is the volume of the prism?", min_value=0.01)
                d = st.number_input("What is the diameter of the base?", min_value=0.01)
                answer = v/(math.pi*((d/2)**2))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The cylinder height is ", answer, " units.")

    if mode == "Cone":
        circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))

        if circlemode == "Radius":
            st.latex(r"V = \frac{r^2πh}{3}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Radius", "Height"))
            if var == "Radius":
                st.latex(r"r = \sqrt{\frac{3V}{πh}}")
                v = st.number_input("What is the volume of the cone?", min_value=0.01)
                h = st.number_input("What is the height of the cone?", min_value=0.01)
                answer = math.sqrt((3*v)/(math.pi*h))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The radius is ", answer, " units.")

            if var == "Height":
                st.latex(r"h = \frac{3V}{πr²}")
                v = st.number_input("What is the volume of the cone?", min_value=0.01)
                r = st.number_input("What is the radius of the cone?", min_value=0.01)
                answer = (3*v)/(math.pi*r**2)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The height is ", answer, " units.")

        if circlemode == "Diameter":
            st.latex(r"V = \frac{(\frac{d}{2})^2πh}{3}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = height</p>""", unsafe_allow_html=True)
            var = st.selectbox("Which variable would you like to calculate?", ("Diameter", "Height"))

            if var == "Diameter":
                st.latex(r"d = 2\sqrt{\frac{3V}{πh}}")
                v = st.number_input("What is the volume of the cone?", min_value=0.01)
                h = st.number_input("What is the height of the cone?", min_value=0.01)
                answer = 2*(math.sqrt((3*v)/(math.pi*h)))
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The diameter is ", answer, " units.")

            if var == "Height":
                st.latex(r"h = \frac{3V}{(\frac{d}{2})²π}")
                v = st.number_input("What is the volume of the cone?", min_value=0.01)
                d = st.number_input("What is the diameter of the base?", min_value=0.01)
                answer = (3*v)/(((d/2)**2)*math.pi)
                if answer < 0:
                    st.write("Invalid circumstances.")
                else:
                    st.write("The height is ", answer, " units.")

    if mode == "Sphere":

        circlemode = st.selectbox("Do you have the diameter or the radius?", ("Radius", "Diameter"))


        if circlemode == "Radius":
            st.latex(r"V = \frac{4}{3}πr^3")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius</p>""", unsafe_allow_html=True)
            st.warning("You are calculating the radius.")
            st.latex(r"r = \sqrt[3]{\frac{V}{\frac{4π}{3}}}")
            v = st.number_input("What is the volume of the sphere?", min_value=0.01)
            answer = math.cbrt(v/(4*math.pi/3))
            if answer < 0:
                st.write("Invalid circumstances.")
            else:
                st.write("The radius is ", answer, " units.")

        if circlemode == "Diameter":
            st.latex(r"V = \frac{4}{3}π(\frac{d}{2})^3")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter</p>""", unsafe_allow_html=True)
            st.warning("You are calculating the diameter.")
            st.latex(r"d = 2\sqrt[3]{\frac{V}{\frac{4π}{3}}}")
            v = st.number_input("What is the volume of the sphere?", min_value=0.01)
            answer = 2*math.cbrt(v/((4*math.pi)/3))
            if answer < 0:
                st.write("Invalid circumstances.")
            else:
                st.write("The diameter is ", answer, " units.")










        
if mnmode == "Surface Area":
    mode = st.selectbox("Which 3D shape's variable would you like to calculate", ("Prism", "Pyramid", "Cylinder", "Cone", "Sphere"))

    if mode == "Prism":
        base = st.number_input("How many sides does your prism's base have?", min_value=3)

        if base == 3:
            st.latex(r"A = bh+H(b+x+y)")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base, h = height, H = prism height, x = side 2 length, y = side 3 length</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Base Base", "Base Height", "Prism Height", "x", "y"))
            if var == "Base Base":
                st.latex(r"b = \frac{A-H(x+y)}{h+H}")
                sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                bh = st.number_input("What is the height of the base?", min_value=0.01)
                ph = st.number_input("What is the prism height?", min_value=0.01)
                x = st.number_input("What is the length of the second side?", min_value=0.01)
                y = st.number_input("What is the length of the third side?", min_value=0.01)
                answer = (sa-(ph*(x+y)))/(bh+ph)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The base's base is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"H = \frac{A}{b+x+y}-bh")
                sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                b = st.number_input("What is the base's base length?", min_value=0.01)
                x = st.number_input("What are the triangles' second side?", min_value=0.01)
                y = st.number_input("What are the triangles' third side?", min_value=0.01)
                h = st.number_input("What is the base's height", min_value=0.01)
                answer = ((sa)/(b+x+y))-(b*h)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The prism height is ", answer, " units.")

            if var == "Base Height":
                st.latex(r"h = \frac{A-H(b+x+y)}{b}")
                sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                b = st.number_input("What is the base's base length?", min_value=0.01)
                x = st.number_input("What is the base's second side?", min_value=0.01)
                y = st.number_input("What is the base's third side?", min_value=0.01)
                answer = (sa - (ph*(x+y+b)))/b
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The base's height is ", answer, " units.")

            if var == "x":
                st.latex(r"x = \frac{A-bh-H(x+y)}{H}")
                sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                b = st.number_input("What is the base's base length?", min_value=0.01)
                h = st.number_input("What is the base's height", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                y = st.number_input("What is the base's third side?", min_value=0.01)
                answer = (sa-(b*h)-ph*(b+y))/ph
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("x is ", answer, " units.")

            if var == "y":
                st.latex(r"y = \frac{A-bh-H(b+x)}{H}")
                sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                b = st.number_input("What is the base's base length?", min_value=0.01)
                h = st.number_input("What is the base's height", min_value=0.01)
                ph = st.number_input("What is the height of the prism?", min_value=0.01)
                x = st.number_input("What is the base's second side?", min_value=0.01)
                answer = (sa-(b*h)-ph*(b+x))/ph
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("y is ", answer, " units.")


        if base == 4:

            fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))

            if fourmode == "Common":
                st.latex(r"A = 2(bh+bH+hH)")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base, h = base height, H = prism height</p>""", unsafe_allow_html=True)
                var = st.selectbox("What variable would you like to solve for?", ("Base", "Base Height", "Prism Height" ))

                if var == "Base":
                    st.latex(r"b = \frac{\frac{A}{2}-hH}{h+H}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    bh = st.number_input("What is the height of the base?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    answer = ((sa/2)-(bh*ph))/(ph+bh)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The base is ", answer, " units.")

                if var == "Base Height":
                    st.latex(r"h = \frac{\frac{A}{2}-bH}{b+H}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    b = st.number_input("What is the length of the base?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    answer = ((sa/2)-(b*ph))/(b+ph)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The base's height is ", answer, " units.")

                if var == "Prism Height":
                    st.latex(r"H = \frac{\frac{A}{2}-bh}{b+h}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    bh = st.number_input("What is the height of the base?", min_value=0.01)
                    b = st.number_input("What is the base length?", min_value=0.01)
                    answer = ((sa/2)-(b*bh))/(b+bh)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The prism height is ", answer, " units.")
                
            if fourmode == "Trapezoid":
                st.latex(r"A = h(a+b)+H(a+b+x+y)")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">a = top side, b = bottom side, x = third side, y = fourth side, h = height, H = prism height</p>""", unsafe_allow_html=True)
                var = st.selectbox("Which variable would you like to calculate for?", ("a", "b", "Third Side", "Fourth Side", "Base Height", "Prism Height"))
                
                if var == "a":
                    st.latex(r"a = \frac{A-hb-H(b+x+y)}{h+H}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    h = st.number_input("What is the height of the base?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    x = st.number_input("What is the length of the third side of the base?", min_value=0.01)
                    y = st.number_input("What is the length of the fourth side of the base?", min_value=0.01)
                    answer = (sa-(b*h)-(ph*(b+x+y)))/(h+ph)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("a is ", answer, " units.")

                if var == "b":
                    st.latex(r"b = \frac{A-ha-H(a+x+y)}{h+H}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    h = st.number_input("What is the height of the base?", min_value=0.01)
                    a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    x = st.number_input("What is the length of the third side of the base?", min_value=0.01)
                    y = st.number_input("What is the length of the fourth side of the base?", min_value=0.01)
                    answer = (sa-h*a-ph*(a+x+y))/(h+ph)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("b is ", answer, " units.")

                if var == "Base Height":
                    st.latex(r"h = \frac{A-H(a+b+x+y)}{a+b}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    x = st.number_input("What is the length of the third side of the base?", min_value=0.01)
                    y = st.number_input("What is the length of the fourth side of the base?", min_value=0.01)
                    answer = (sa-(ph*(a+b+x+y)))/(a+b)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The base height is ", answer, " units.")

                if var == "Prism Height":
                    st.latex(r"H = \frac{A-h(a+b)}{a+b+x+y}")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    h = st.number_input("What is the base height?", min_value=0.01)
                    x = st.number_input("What is the length of the third side of the base?", min_value=0.01)
                    y = st.number_input("What is the length of the fourth side of the base?", min_value=0.01)
                    answer = (sa-(h*(a+b)))/(a+b+x+y)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The prism height is ", answer, " units.")

                if var == "Third Side":
                    st.latex(r"x = \frac{A-h(a+b)}{H}-(a+b+y)")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    h = st.number_input("What is the base height?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    y = st.number_input("What is the length of the fourth side of the base?", min_value=0.01)       
                    answer = ((sa-(h*(a+b)))/ph)-(a+b+y)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The third side's length is ", answer, " units.")

                if var == "Fourth Side":
                    st.latex(r"y = \frac{A-h(a+b)}{H}-(a+b+x)")
                    sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                    a = st.number_input("What is a (opposite to b)?", min_value=0.01)
                    b = st.number_input("What is b (opposite to a)?", min_value=0.01)
                    h = st.number_input("What is the base height?", min_value=0.01)
                    ph = st.number_input("What is the prism height?", min_value=0.01)
                    x = st.number_input("What is the length of the third side of the base?", min_value=0.01)       
                    answer = ((sa-(h*(a+b)))/ph)-(a+b+x)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The fourth side's length is ", answer, " units.")

        if base > 4:
            #could be wrong in main.py
            st.warning("Prisms with bases with more than 5 sides will only calculate shapes with regular bases.")
            st.latex(r"S = AP+ehs")      
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, e = edge length, h = prism height, s = no. of sides</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Apothem", "Perimieter", "Edge Length", "Prism Height"))
            if var == "Apothem":
                st.latex(r"A = \frac{e}{2tan(\frac{180}{s})}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">s = no. of sides</p>""", unsafe_allow_html=True)
                e = st.number_input("What is the edge length?", min_value=0.01)
                answer = (e / (2 * math.tan(math.radians(180 / base))))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The prism's apothem is ", answer, " units.")

            if var == "Perimieter":
                st.latex(r"P = es")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">s = no. of sides</p>""", unsafe_allow_html=True)
                e = st.number_input("What is the edge length?", min_value=0.01)
                answer = e*base
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The perimeter is ", answer, " units.")

            if var == "Edge Length":
                st.latex(r"e = \frac{P}{s}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">s = no. of sides</p>""", unsafe_allow_html=True)
                p = st.number_input("What is the perimeter of the prism's base?", min_value=0.01)
                answer = p/base
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The edge length is ", answer, " units.")

            if var == "Prism Height":
                st.latex(r"h = \frac{S-AP}{es}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">s = no. of sides</p>""", unsafe_allow_html=True)
                sa = st.number_input("What is the surface area of the prism?", min_value=0.01)
                e = st.number_input("What is the edge length of the base?", min_value=0.01)
                answer = (sa-((e / (2 * math.tan(math.radians(180 / base))))*(e*base)))/((e*base))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The height is ", answer, " units.")


    if mode == "Pyramid":
        base = st.number_input("How many sides does your pyramid's base have?", min_value=3)

        if base == 3:
            st.latex(r"A = \frac{bh+s(b+x+y)}{2}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base's base, h = base's height, s = slant height, x = second side, y = third side</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Base's Base", "Base's Height", "Slant Height", "Base's Second Side", "Base's Third Side"))
            if var == "Base's Base":
                st.latex(r"b = \frac{2A-s(x+y)}{h+s}")
                sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                s = st.number_input("What is the slant height of the upper-triangles?", min_value=0.01)
                x = st.number_input("What is the second side of the base?", min_value=0.01)
                y = st.number_input("What is the third side of the base?", min_value=0.01)
                h = st.number_input("What is the height of the triangle?", min_value=0.01)
                answer = ((2*sa)-s*(x+y))/(h+s)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The base's base length is ", answer, " units.")

            if var == "Base's Height":
                st.latex(r"h = \frac{2A-s(b+x+y)}{b}")
                sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                s = st.number_input("What is the slant height of the upper-triangles?", min_value=0.01)
                b = st.number_input("What is the base's base length?", min_value=0.01)
                x = st.number_input("What is the length of the second side of the triangle?", min_value=0.01)
                y = st.number_input("What is the length of the third side of the triangle?", min_value=0.01)
                answer = ((2*sa)-(s*(b+x+y)))/b
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The base's height is ", answer, " units.")

            if var == "Base's Second Side":
                st.latex(r"x = \frac{2A-bh}{s}-(b+y)")
                sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                b = st.number_input("What is the base length?", min_value=0.01)
                h = st.number_input("What is the base's height?", min_value=0.01)
                s = st.number_input("What is the slant height?", min_value=0.01)
                y = st.number_input("What is the length of the base's third side?", min_value=0.01)
                answer = (((2*sa)-(b*h))/s)-(b+y)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The base's second side is", answer, " units.")

            if var == "Base's Third Side":
                st.latex(r"y = \frac{2A-bh}{s}-(b+x)")
                sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                b = st.number_input("What is the base length?", min_value=0.01)
                h = st.number_input("What is the base's height?", min_value=0.01)
                s = st.number_input("What is the slant height?", min_value=0.01)
                x = st.number_input("What is the length of the base's second side?", min_value=0.01)
                answer = (((2*sa)-(b*h))/s)-(b+x)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The base's third side is", answer, " units.")

            if var == "Slant Height":
                st.latex(r"s = \frac{2A-bh}{b+x+y}")
                sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                b = st.number_input("What is the base length?", min_value=0.01)
                h = st.number_input("What is the base's height?", min_value=0.01)
                x = st.number_input("What is the base's second side?", min_value=0.01)
                y = st.number_input("What is the base's third side?", min_value=0.01)
                answer = ((2*sa)-(b*h))/(b+x+y)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The slant height is ", answer, " units")

        if base == 4:

            fourmode = st.selectbox("Do you have a common base or a trapezoid base?", ("Common", "Trapezoid"))
                        
            if fourmode == "Common":
                st.latex(r"A = bh+s(b+h)")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">b = base length, h = base height, s = slant</p>""", unsafe_allow_html=True)
                var = st.selectbox("What variable would you like to calculate for?", ("Base Length", "Base Height", "Slant"))
                if var == "Base Length":
                    st.latex(r"b = \frac{A-sh}{s+h}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height of the pyramid?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    answer = (sa-(s*h))/(s+h)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The base's length is ", answer, " units.")

                if var == "Base Height":
                    st.latex(r"h = \frac{A-sb}{b+s}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height?", min_value=0.01)
                    b = st.number_input("What is the base length?", min_value=0.01)
                    answer = (sa-(s*b))/(b+s)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The base's height is ", answer, " units.")

                if var == "Slant":
                    st.latex(r"s = \frac{A-bh}{b+h}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    b = st.number_input("What is the base's length?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    answer = (sa-(b*h))/(b+h)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The slant height is ", answer, " units.")

            if fourmode == "Trapezoid":
                st.latex(r"A = \frac{s(a+b+x+y)+h(a+b)}{2}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">h = height, a = base top side, b = base bottom side, x = third side, y = fourth side, s = slant</p>""", unsafe_allow_html=True)
                var = st.selectbox("What variable would you like to calculate for?", ("Base Height", "a", "b", "x", "y", "Slant"))
                if var == "Base Height":
                    st.latex(r"h = \frac{2A-s(a+b+x+y)}{a+b}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height?", min_value=0.01)
                    x = st.number_input("What is the third side of the base's length?", min_value=0.01)
                    y = st.number_input("What is the fourth side of the base's length?", min_value=0.01)
                    a = st.number_input("What is a's length (top or bottom side)?", min_value=0.01)
                    b = st.number_input("What is b's length (opposite to a)?", min_value=0.01)
                    answer = (2*sa-s*(a+b+x+y))/(a+b)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The base's height is ", answer, " units.")

                if var == "a":
                    st.latex(r"a = \frac{2A-hb-s(b+x+y)}{s+h}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height?", min_value=0.01)
                    x = st.number_input("What is the third side of the base's length?", min_value=0.01)
                    y = st.number_input("What is the fourth side of the base's length?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    b = st.number_input("What is b's length (opposite to a)?", min_value=0.01)
                    answer = ((2*sa)-h*b-s*(b+x+y))/(s+h)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("a is ", answer, " units.")

                if var == "b":
                    st.latex(r"b = \frac{2A-ha-s(a+x+y)}{s+h}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height?", min_value=0.01)
                    x = st.number_input("What is the third side of the base's length?", min_value=0.01)
                    y = st.number_input("What is the fourth side of the base's length?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    a = st.number_input("What is a's length (opposite to b)?", min_value=0.01)
                    answer = ((2*sa)-h*a-s*(a+x+y))/(s+h)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("b is ", answer, " units.")

                if var == "x":
                    st.latex(r"x = \frac{2A-h(a+b)}{s}-(a+b+y)")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height?", min_value=0.01)
                    y = st.number_input("What is the fourth side of the base's length?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    a = st.number_input("What is a's length (top or bottom side of base)?", min_value=0.01)
                    b = st.number_input("What is b's length (opposite to a)?", min_value=0.01)
                    answer = (((2*sa)-h*(a+b))/(s))-(a+b+y)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("x (base's third side) is ", answer, " units.")

                if var == "y":
                    st.latex(r"y = \frac{2A-h(a+b)}{s}-(a+b+x)")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    s = st.number_input("What is the slant height?", min_value=0.01)
                    x = st.number_input("What is the third side of the base's length?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    a = st.number_input("What is a's length (top or bottom side of base)?", min_value=0.01)
                    b = st.number_input("What is b's length (opposite to a)?", min_value=0.01)
                    answer = (((2*sa)-h*(a+b))/(s))-(a+b+x)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("y (base's fourth side) is ", answer, " units.")

                if var == "Slant":
                    st.latex(r"s = \frac{2A-h(a+b)}{a+b+x+y}")
                    sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                    x = st.number_input("What is the third side of the base's length?", min_value=0.01)
                    y = st.number_input("What is the fourth side of the base's length?", min_value=0.01)
                    h = st.number_input("What is the base's height?", min_value=0.01)
                    a = st.number_input("What is a's length (top or bottom side of base)?", min_value=0.01)
                    b = st.number_input("What is b's length (opposite to a)?", min_value=0.01)
                    answer = ((2*sa)-(h*(a+b)))/(a+b+x+y)
                    if answer < 0:
                        st.write("Invalid circumstances.") 
                    else:
                        st.write("The slanth height is", answer, " units.")
                
        if base > 4:
            #formula could be wrong in main/py
            st.warning("Pyramids with bases with more than 5 sides will only calculate shapes with regular bases.")
            st.latex(r"S = \frac{AP+esx}{2}")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">A = apothem, P = perimeter, x = no. of sides, e = edge length, s = slant</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Apothem", "Perimeter", "Edge Length", "Slant"))
            if var == "Apothem":
                st.latex(r"A = \frac{e}{2tan(\frac{180}{x})}")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides</p>""", unsafe_allow_html=True)
                e = st.number_input("What is the edge length?", min_value=0.01)
                answer = (e / (2 * math.tan(math.radians(180 / base))))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The prism's apothem is ", answer, " units.")

            if var == "Perimeter":
                st.latex(r"P = ex")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides</p>""", unsafe_allow_html=True)
                e = st.number_input("What is the edge length?", min_value=0.01)
                answer = e*base
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The perimeter is ", answer, " units.")

            if var == "Edge Length":
                st.latex(r"e = P/x")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides</p>""", unsafe_allow_html=True)
                p = st.number_input("What is the perimeter of the base?")
                answer = p/base
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The edge length is ", answer, " units.")

            if var == "Slant":
                st.latex(r"S = \frac{2S}{xe}-A")
                st.markdown("""<p style="text-align: center; padding-bottom: 10px;">x = no. of sides</p>""", unsafe_allow_html=True)
                sa = st.number_input("What is the surface area of the pyramid?", min_value=0.01)
                e = st.number_input("What is the edge length?", min_value=0.01)
                answer = ((2*sa)-(((e / (2 * math.tan(math.radians(180 / base))))))*(e*base))/base*e
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The slant height is ", answer, " units.")

    if mode == "Cylinder":
        circmode = st.selectbox("Do you have the radius or diameter?", ("Radius", "Diameter"))
            
        if circmode == "Radius":
            st.latex(r"A = πr²+Ch")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, C = circumference, h = prism height</p>""", unsafe_allow_html=True)     
            var = st.selectbox("What variable would you like to calculate?", ("Radius", "Height"))

            if var == "Radius":
                st.latex(r"r = \frac{-2πh+\sqrt{4π²h²+8πA}}{4π}")
                sa = st.number_input("What is the surface area?", min_value=0.01)
                h = st.number_input("What is the height?", min_value=0.01)
                answer = (-2 * math.pi * h + math.sqrt(4 * math.pi**2 * h**2 + 8 * math.pi * sa)) / (4 * math.pi)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The radius is ", answer, " units.")

            if var == "Height":
                st.latex(r"h = \frac{A}{2πr}-r")
                sa = st.number_input("What is the surface area of the cylinder?", min_value=0.01)
                r = st.number_input("What is the radius of the cylinder?", min_value=0.01)
                answer = (sa/(2*math.pi*r))-r
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The prism hiehgt is ", answer, " units.")

        if circmode == "Diameter":
            st.latex(r"A = π(\frac{d}{2})²+Ch")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, C = circumference, h = prism height</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Diameter", "Height"))

            if var == "Diameter":
                st.latex(r"d = 2(\frac{-2πh+\sqrt{4π²h²+8πA}}{4π})")
                sa = st.number_input("What is the surface area?", min_value=0.01)
                h = st.number_input("What is the height?", min_value=0.01)
                answer = 2*((-2 * math.pi * h + math.sqrt(4 * math.pi**2 * h**2 + 8 * math.pi * sa)) / (4 * math.pi))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The radius is ", answer, " units.")

            if var == "Height":
                st.latex(r"h = \frac{A}{2π\frac{d}{2}}-\frac{d}{2}")
                sa = st.number_input("What is the surface area?", min_value=0.01)
                d = st.number_input("What is the diameter?", min_value=0.01)
                answer  = ((sa)/(2*math.pi*(d/2)))-(d/2)
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The height is ", answer, " units.")

    if mode == "Cone":
        circmode = st.selectbox("Do you have the radius or diameter?", ("Radius", "Diameter"))
            
        if circmode == "Radius":
            st.latex(r"A = πr(r+\sqrt{h²+r²})")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius, h = cone height</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Radius", "Cone Height"))
            if var == "Radius":
                st.latex(r"r = \sqrt{(\frac{A²}{π(πh²+2A)}})")
                sa = st.number_input("What is the surface area of the cone?", min_value=0.01)
                h = st.number_input("What is the height of the cone?", min_value=0.01)
                answer = math.sqrt((sa**2)/(math.pi*(math.pi*h**2+(2*sa))))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The radius is ", answer, " units.")

            if var == "Cone Height":
                st.latex(r"h = \sqrt{(\frac{A}{πr})²-\frac{2A}{π}}")
                sa = st.number_input("What is the surface area of the cone?", min_value=0.01)
                r = st.number_input("What is the radius?", min_value=0.01)
                answer = math.sqrt((sa / (math.pi * r))**2 - (2 * sa / math.pi))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The height is ", answer, " units.")

        if circmode == "Diameter":

            st.latex(r"A = π(\frac{d}{2})((\frac{d}{2})+\sqrt{h²+(\frac{d}{2})²})")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter, h = cone height</p>""", unsafe_allow_html=True)
            var = st.selectbox("What variable would you like to calculate?", ("Diameter", "Cone Height"))
            if var == "Diameter":
                st.latex(r"d = 2(\sqrt{\frac{A²}{π(πh²+2A)}})")
                sa = st.number_input("What is the surface area of the cone?", min_value=0.01)
                h = st.number_input("What is the height of the cone?", min_value=0.01)
                answer = 2*(math.sqrt((sa**2)/(math.pi*(math.pi*h**2+(2*sa)))))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The diameter is ", answer, " units.")

            if var == "Cone Height":
                st.latex(r"h = \sqrt{(\frac{A}{π\frac{d}{2}})²-\frac{2A}{π}}")
                sa = st.number_input("What is the surface area of the cone?", min_value=0.01)
                d = st.number_input("What is the diameter?", min_value=0.01)
                answer = math.sqrt((sa / (math.pi * (d / 2)))**2 - (2 * sa / math.pi))
                if answer < 0:
                    st.write("Invalid circumstances.") 
                else:
                    st.write("The height is ", answer, " units.")

    if mode == "Sphere":
        circmode = st.selectbox("Do you have the radius or diameter?", ("Radius", "Diameter"))
            
        if circmode == "Radius":
            st.latex(r"A = 4πr²")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">r = radius</p>""", unsafe_allow_html=True)
            st.warning("You can only calculate the radius.")
            st.latex(r"r = \sqrt{\frac{A}{4π}}")
            sa = st.number_input("What is the surface area?", min_value=0.01)
            answer = math.sqrt(sa/(4*math.pi))
            if answer < 0:
                st.write("Invalid circumstances.") 
            else:
                st.write("The radius is ", answer, " units.")
            

        if circmode == "Diameter":
            st.latex(r"A = 4π(\frac{d}{2})²")
            st.markdown("""<p style="text-align: center; padding-bottom: 10px;">d = diameter</p>""", unsafe_allow_html=True)
            st.warning("You can only calculate the diameter.")
            st.latex(r"d = 2\sqrt{\frac{A}{4π}}")
            sa = st.number_input("What is the surface area?", min_value=0.01)
            answer = 2*(math.sqrt(sa/(4*math.pi)))
            if answer < 0:
                st.write("Invalid circumstances.") 
            else:
                st.write("The diameter is ", answer, " units.")
