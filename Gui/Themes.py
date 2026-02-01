
from Gui import Colors
from Gui import Fonts


class Theme:
    SplitterBackgroundColor = Colors.COLOR_VSC_SECONDARY

    ScrollHorizontalHandleBackgroundColor = Colors.COLOR_VSC_LIGHT
    ScrollHorizontalBorderColor           = Colors.COLOR_VSC_SECONDARY
    ScrollHorizontalBorderRadius          = 0
    ScrollHorizontalHandleBorderRadius    = 0
    ScrollHorizontalMinWidth              = 128
    ScrollHorizontalHeight                = 20
    ScrollVerticalHandleBackgroundColor   = Colors.COLOR_VSC_LIGHT
    ScrollVerticalBorderColor             = Colors.COLOR_VSC_SECONDARY
    ScrollVerticalBorderRadius            = 0
    ScrollVerticalHandleBorderRadius      = 0
    ScrollVerticalMinHeight               = 128
    ScrollVerticalWidth                   = 20

    ScrollPreHorizontalHandleBackgroundColor = Colors.COLOR_BS_LIGHT
    ScrollPreHorizontalBorderColor           = Colors.COLOR_BS_LIGHT
    ScrollPreHorizontalBorderRadius          = 0
    ScrollPreHorizontalHandleBorderRadius    = 0
    ScrollPreHorizontalMinWidth              = 16
    ScrollPreHorizontalHeight                = 16
    ScrollPreVerticalHandleBackgroundColor   = Colors.COLOR_BS_LIGHT
    ScrollPreVerticalBorderColor             = Colors.COLOR_BS_LIGHT
    ScrollPreVerticalBorderRadius            = 0
    ScrollPreVerticalHandleBorderRadius      = 0
    ScrollPreVerticalMinHeight               = 16
    ScrollPreVerticalWidth                   = 16

    WelcomeLogoFont       = Fonts.FONT_GEOLOGICA_BLACK
    WelcomeLogoFontWeight = Fonts.Font.Black
    WelcomeLogoFontSize   = 48
    WelcomeLogoColor      = Colors.COLOR_BS_LIGHT

    WelcomeOpenProjectFont       = Fonts.FONT_GEOLOGICA_BLACK
    WelcomeOpenProjectFontWeight = Fonts.Font.Black
    WelcomeOpenProjectFontSize   = 18
    WelcomeOpenProjectColor      = Colors.COLOR_BS_LIGHT

    DashboardScreenBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBorderColor     = Colors.COLOR_VSC_TERTIARY
    DashboardBodyBackgroundColor   = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBorderColor     = Colors.COLOR_VSC_TERTIARY

    DashboardReportsListSectionBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportSectionBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    
    DashboardNoReportSelectedFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardNoReportSelectedFontWeight = Fonts.Font.Black
    DashboardNoReportSelectedFontSize   = 16
    DashboardNoReportSelectedColor      = Colors.COLOR_VSC_LIGHT

    DashboardNoReportsFoundFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardNoReportsFoundFontWeight = Fonts.Font.Black
    DashboardNoReportsFoundFontSize   = 16
    DashboardNoReportsFoundColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportCardBackgroundColor        = Colors.COLOR_VSC_PRIMARY
    DashboardReportCardBorderColor            = Colors.COLOR_VSC_TERTIARY
    DashboardReportCardHoveredBackgroundColor = Colors.COLOR_VSC_SECONDARY

    DashboardReportCardTitleFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportCardTitleFontWeight = Fonts.Font.Black
    DashboardReportCardTitleFontSize   = 11
    DashboardReportCardTitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportCardIdFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportCardIdFontWeight = Fonts.Font.ExtraLight
    DashboardReportCardIdFontSize   = 9
    DashboardReportCardIdColor      = Colors.COLOR_VSC_QUATERNARY
    
    DashboardReportCardPropertyEmojiFont     = Fonts.FONT_SEGOE_UI_EMOJI
    DashboardReportCardPropertyEmojiFontSize = 12

    DashboardReportCardPropertyNameFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportCardPropertyNameFontWeight = Fonts.Font.Black
    DashboardReportCardPropertyNameFontSize   = 10
    DashboardReportCardPropertyNameColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportCardPropertyValueFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportCardPropertyValueFontWeight = Fonts.Font.ExtraLight
    DashboardReportCardPropertyValueFontSize   = 10
    DashboardReportCardPropertyValueColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetTitleFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportWidgetTitleFontWeight = Fonts.Font.Black
    DashboardReportWidgetTitleFontSize   = 13
    DashboardReportWidgetTitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetIdFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportWidgetIdFontWeight = Fonts.Font.ExtraLight
    DashboardReportWidgetIdFontSize   = 11
    DashboardReportWidgetIdColor      = Colors.COLOR_VSC_QUATERNARY

    DashboardReportWidgetPropertyEmojiFont     = Fonts.FONT_SEGOE_UI_EMOJI
    DashboardReportWidgetPropertyEmojiFontSize = 12

    DashboardReportWidgetPropertyNameFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportWidgetPropertyNameFontWeight = Fonts.Font.Black
    DashboardReportWidgetPropertyNameFontSize   = 11
    DashboardReportWidgetPropertyNameColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetPropertyValueFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportWidgetPropertyValueFontWeight = Fonts.Font.ExtraLight
    DashboardReportWidgetPropertyValueFontSize   = 11
    DashboardReportWidgetPropertyValueColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetSubtitleFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportWidgetSubtitleFontWeight = Fonts.Font.Black
    DashboardReportWidgetSubtitleFontSize   = 11
    DashboardReportWidgetSubtitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportItemPFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportItemPFontWeight = Fonts.Font.ExtraLight
    DashboardReportItemPFontSize   = 11
    DashboardReportItemPColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportItemPreBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportItemPreFont            = Fonts.FONT_JET_BRAINS_MONO_NL_REGULAR
    DashboardReportItemPreFontWeight      = Fonts.Font.ExtraLight
    DashboardReportItemPreFontSize        = 10
    DashboardReportItemPreColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportItemPreBorderRadius    = 0


class DefaultTheme(Theme):
    pass


CurrentTheme = DefaultTheme
