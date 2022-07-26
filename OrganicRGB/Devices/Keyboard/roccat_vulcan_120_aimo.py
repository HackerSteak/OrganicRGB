from OrganicRGB.DeviceTypes.Keyboard import german_keys

class main:
    height = 234 #mm
    length = 463 #mm
    name = 'Roccat Vulcan 120 Aimo'

    def __init__(self):
        self.keys = german_keys()
        self.define_keys()

    def define_keys(self):
        self.keys.K_Escape(x=27, y=29)
        self.keys.K_Circumflex(x=256, y=53)
        self.keys.K_Tab(x=31, y=71)
        self.keys.K_Caps_Lock(x=33, y=90)
        self.keys.K_Left_Shift(x=28, y=109)
        self.keys.K_Left_Control(x=28, y=129)
        self.keys.K_1(x=46, y=52)
        self.keys.K_Q(x=55, y=72)
        self.keys.K_A(x=60, y=91)
        self.keys.K_Lessthan(x=50, y=110)
        self.keys.K_Left_Windows(x=52, y=130)
        self.keys.K_F1(x=64, y=27)
        self.keys.K_2(x=64, y=52)
        self.keys.K_W(x=74, y=71)
        self.keys.K_S(x=79, y=91)
        self.keys.K_Y(x=70, y=110)
        self.keys.K_Left_Alt(x=76, y=129)
        self.keys.K_F2(x=83, y=28)
        self.keys.K_3(x=83, y=54)
        self.keys.K_E(x=93, y=72)
        self.keys.K_D(x=98, y=91)
        self.keys.K_X(x=88, y=111)
        self.keys.K_F3(x=102, y=29)
        self.keys.K_4(x=103, y=52)
        self.keys.K_R(x=112, y=71)
        self.keys.K_F(x=117, y=91)
        self.keys.K_C(x=107, y=110)
        self.keys.K_F4(x=121, y=28)
        self.keys.K_5(x=121, y=51)
        self.keys.K_T(x=131, y=71)
        self.keys.K_G(x=136, y=91)
        self.keys.K_V(x=126, y=110)
        self.keys.K_6(x=140, y=52)
        self.keys.K_Z(x=150, y=72)
        self.keys.K_H(x=155, y=91)
        self.keys.K_B(x=146, y=110)
        self.keys.K_Space(x=147, y=129)
        self.keys.K_F5(x=150, y=29)
        self.keys.K_7(x=160, y=53)
        self.keys.K_U(x=170, y=72)
        self.keys.K_J(x=174, y=91)
        self.keys.K_N(x=165, y=110)
        self.keys.K_F6(x=170, y=28)
        self.keys.K_8(x=179, y=52)
        self.keys.K_I(x=189, y=71)
        self.keys.K_K(x=193, y=91)
        self.keys.K_M(x=184, y=110)
        self.keys.K_F7(x=189, y=28)
        self.keys.K_9(x=218, y=52)
        self.keys.K_O(x=208, y=71)
        self.keys.K_L(x=213, y=92)
        self.keys.K_Comma(x=203, y=110)
        self.keys.K_F8(x=293, y=28)
        self.keys.K_0(x=218, y=51)
        self.keys.K_P(x=227, y=72)
        self.keys.K_OE(x=232, y=92)
        self.keys.K_Dot(x=222, y=110)
        self.keys.K_Right_Alt(x=220, y=129)
        self.keys.K_Sharp_S(x=237, y=53)
        self.keys.K_UE(x=246, y=71)
        self.keys.K_AE(x=270, y=91)
        self.keys.K_Minus(x=242, y=110)
        self.keys.K_Right_Fn(x=244, y=129)
        self.keys.K_F9(x=237, y=28)
        self.keys.K_Acute_Accent(x=256, y=53)
        self.keys.K_Plus(x=265, y=72)
        self.keys.K_Right_Shift(x=277, y=110)
        self.keys.K_Menu(x=268, y=129)
        self.keys.K_F10(x=256, y=28)
        self.keys.K_F11(x=275, y=28)
        self.keys.K_F12(x=294, y=28)
        self.keys.K_Backspace(x=285, y=53)
        self.keys.K_Enter(x=291, y=80)
        self.keys.K_Right_Control(x=292, y=130)
        self.keys.K_Hashtag(x=270, y=91)
        self.keys.K_Print_Screen(x=318, y=28)
        self.keys.K_Insert(x=318, y=52)
        self.keys.K_Delete(x=318, y=72)
        self.keys.K_Left_Arrow(x=318, y=130)
        self.keys.K_Scroll_Lock(x=337, y=28)
        self.keys.K_Home(x=337, y=53)
        self.keys.K_End(x=337, y=73)
        self.keys.K_Up_Arrow(x=337, y=111)
        self.keys.K_Down_Arrow(x=337, y=130)
        self.keys.K_Pause_Break(x=356, y=28)
        self.keys.K_Page_Up(x=356, y=53)
        self.keys.K_Page_Down(x=356, y=73)
        self.keys.K_Right_Arrow(x=356, y=130)
        self.keys.K_Num_Lock(x=381, y=54)
        self.keys.K_Number_Pad_7(x=381, y=72)
        self.keys.K_Number_Pad_4(x=381, y=92)
        self.keys.K_Number_Pad_1(x=381, y=110)
        self.keys.K_Number_Pad_0(x=390, y=130)
        self.keys.K_Number_Pad_Slash(x=400, y=54)
        self.keys.K_Number_Pad_8(x=400, y=72)
        self.keys.K_Number_Pad_5(x=400, y=72)
        self.keys.K_Number_Pad_2(x=400, y=110)
        self.keys.K_Number_Pad_Star(x=419, y=54)
        self.keys.K_Number_Pad_9(x=419, y=72)
        self.keys.K_Number_Pad_6(x=419, y=72)
        self.keys.K_Number_Pad_3(x=419, y=110)
        self.keys.K_Number_Pad_Comma(x=419, y=130)
        self.keys.K_Number_Pad_Minus(x=438, y=54)
        self.keys.K_Number_Pad_Plus(x=438, y=83)
        self.keys.K_Number_Pad_Enter(x=438, y=121)
