
import sys

from Gui import Colors
from Gui import Fonts

THEME_DEFAULT = 'Default'
THEME_DARK = 'Dark'
THEME_LIGHT = 'Light'


class Theme:
    NAME = THEME_DEFAULT

    SplitterBackgroundColor = Colors.COLOR_VSC_SECONDARY

    ScrollHorizontalBackgroundColor       = Colors.COLOR_VSC_PRIMARY
    ScrollHorizontalHandleBackgroundColor = Colors.COLOR_VSC_LIGHT
    ScrollHorizontalBorderColor           = Colors.COLOR_VSC_SECONDARY
    ScrollHorizontalBorderRadius          = 0
    ScrollHorizontalHandleBorderRadius    = 0
    ScrollHorizontalMinWidth              = 128
    ScrollHorizontalHeight                = 20
    ScrollVerticalBackgroundColor         = Colors.COLOR_VSC_PRIMARY
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
    DashboardBodyBorderColor       = Colors.COLOR_VSC_TERTIARY
    DashboardFooterBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBorderColor     = Colors.COLOR_VSC_TERTIARY

    DashboardReloadProjectFont                 = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReloadProjectFontWeight           = Fonts.Font.Black
    DashboardReloadProjectFontSize             = 13
    DashboardReloadProjectColor                = Colors.COLOR_VSC_LIGHT
    DashboardReloadProjectHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardReloadProjectBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    DashboardReloadProjectHoverBackgroundColor = Colors.COLOR_VSC_TERTIARY
    DashboardReloadProjectBorderColor          = Colors.COLOR_VSC_SECONDARY

    DashboardSwitchThemeFont                 = Fonts.FONT_GEOLOGICA_BLACK
    DashboardSwitchThemeFontWeight           = Fonts.Font.Black
    DashboardSwitchThemeFontSize             = 13
    DashboardSwitchThemeColor                = Colors.COLOR_VSC_LIGHT
    DashboardSwitchThemeHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardSwitchThemeBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    DashboardSwitchThemeHoverBackgroundColor = Colors.COLOR_VSC_TERTIARY
    DashboardSwitchThemeBorderColor          = Colors.COLOR_VSC_SECONDARY

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

    DashboardReportsListToolsBorderColor = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListSearchQueryFieldFont            = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListSearchQueryFieldFontWeight      = Fonts.Font.Black
    DashboardReportsListSearchQueryFieldFontSize        = 12
    DashboardReportsListSearchQueryFieldColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListSearchQueryFieldBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListSearchQueryFieldBorderColor     = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListCurrentPageFont            = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListCurrentPageFontWeight      = Fonts.Font.Black
    DashboardReportsListCurrentPageFontSize        = 12
    DashboardReportsListCurrentPageColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListCurrentPageBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListCurrentPageBorderColor     = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListPageControlFont                 = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListPageControlFontWeight           = Fonts.Font.Black
    DashboardReportsListPageControlFontSize             = 12
    DashboardReportsListPageControlColor                = Colors.COLOR_VSC_LIGHT
    DashboardReportsListPageControlHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListPageControlBackgroundColor      = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListPageControlHoverBackgroundColor = Colors.COLOR_VSC_SECONDARY
    DashboardReportsListPageControlBorderColor          = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListTotalPagesFont        = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListTotalPagesFontWeight  = Fonts.Font.Black
    DashboardReportsListTotalPagesFontSize    = 12
    DashboardReportsListTotalPagesColor       = Colors.COLOR_VSC_LIGHT
    DashboardReportsListTotalPagesBorderColor = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListPagesLabelFont        = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListPagesLabelFontWeight  = Fonts.Font.Black
    DashboardReportsListPagesLabelFontSize    = 12
    DashboardReportsListPagesLabelColor       = Colors.COLOR_VSC_LIGHT
    DashboardReportsListPagesLabelBorderColor = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListOfPagesLabelFont        = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListOfPagesLabelFontWeight  = Fonts.Font.Black
    DashboardReportsListOfPagesLabelFontSize    = 12
    DashboardReportsListOfPagesLabelColor       = Colors.COLOR_VSC_LIGHT
    DashboardReportsListOfPagesLabelBorderColor = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListSearchFont                 = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListSearchFontWeight           = Fonts.Font.Black
    DashboardReportsListSearchFontSize             = 12
    DashboardReportsListSearchColor                = Colors.COLOR_VSC_LIGHT
    DashboardReportsListSearchHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListSearchBackgroundColor      = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListSearchHoverBackgroundColor = Colors.COLOR_VSC_SECONDARY
    DashboardReportsListSearchBorderColor          = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListNewReportFont                 = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportsListNewReportFontWeight           = Fonts.Font.Black
    DashboardReportsListNewReportFontSize             = 12
    DashboardReportsListNewReportColor                = Colors.COLOR_VSC_LIGHT
    DashboardReportsListNewReportHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListNewReportBackgroundColor      = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListNewReportHoverBackgroundColor = Colors.COLOR_VSC_SECONDARY
    DashboardReportsListNewReportBorderColor          = Colors.COLOR_VSC_SECONDARY

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

    DashboardReportWidgetMargins = (64, 32, 64, 32)

    DashboardReportWidgetTitleFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardReportWidgetTitleFontWeight = Fonts.Font.Black
    DashboardReportWidgetTitleFontSize   = 13
    DashboardReportWidgetTitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetIdFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportWidgetIdFontWeight = Fonts.Font.ExtraLight
    DashboardReportWidgetIdFontSize   = 10
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
    DashboardReportItemPreFontWeight      = Fonts.Font.Regular
    DashboardReportItemPreFontSize        = 9
    DashboardReportItemPreColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportItemPreBorderRadius    = 0


class DarkTheme(Theme):
    NAME = THEME_DARK


class LightTheme(Theme):
    NAME = THEME_LIGHT

    SplitterBackgroundColor = Colors.COLOR_VSC_LIGHT
    
    ScrollHorizontalBackgroundColor       = Colors.COLOR_BS_LIGHT
    ScrollHorizontalHandleBackgroundColor = Colors.COLOR_VSC_LIGHT
    ScrollHorizontalBorderColor           = Colors.COLOR_VSC_LIGHT
    ScrollVerticalBackgroundColor         = Colors.COLOR_BS_LIGHT
    ScrollVerticalHandleBackgroundColor   = Colors.COLOR_VSC_LIGHT
    ScrollVerticalBorderColor             = Colors.COLOR_VSC_LIGHT

    ScrollPreHorizontalHandleBackgroundColor = Colors.COLOR_VSC_LIGHT
    ScrollPreHorizontalBorderColor           = Colors.COLOR_VSC_LIGHT
    ScrollPreVerticalHandleBackgroundColor   = Colors.COLOR_VSC_LIGHT
    ScrollPreVerticalBorderColor             = Colors.COLOR_VSC_LIGHT

    DashboardScreenBackgroundColor = Colors.COLOR_WHITE
    DashboardHeaderBackgroundColor = Colors.COLOR_WHITE
    DashboardHeaderBorderColor     = Colors.COLOR_VSC_LIGHT
    DashboardBodyBackgroundColor   = Colors.COLOR_WHITE
    DashboardBodyBorderColor       = Colors.COLOR_VSC_LIGHT
    DashboardFooterBackgroundColor = Colors.COLOR_WHITE
    DashboardFooterBorderColor     = Colors.COLOR_VSC_LIGHT

    DashboardReloadProjectColor                = Colors.COLOR_BS_DARK
    DashboardReloadProjectHoverColor           = Colors.COLOR_BS_LIGHT
    DashboardReloadProjectBackgroundColor      = 'transparent'
    DashboardReloadProjectHoverBackgroundColor = Colors.COLOR_BS_DARK
    DashboardReloadProjectBorderColor          = Colors.COLOR_BS_DARK

    DashboardSwitchThemeColor                = Colors.COLOR_BS_DARK
    DashboardSwitchThemeHoverColor           = Colors.COLOR_BS_LIGHT
    DashboardSwitchThemeBackgroundColor      = 'transparent'
    DashboardSwitchThemeHoverBackgroundColor = Colors.COLOR_BS_DARK
    DashboardSwitchThemeBorderColor          = Colors.COLOR_BS_DARK

    DashboardReportsListSectionBackgroundColor = Colors.COLOR_WHITE
    DashboardReportSectionBackgroundColor      = Colors.COLOR_WHITE
    
    DashboardNoReportSelectedColor = Colors.COLOR_BS_DARK
    DashboardNoReportsFoundColor   = Colors.COLOR_BS_DARK

    DashboardReportsListToolsBorderColor = Colors.COLOR_VSC_LIGHT

    DashboardReportsListSearchQueryFieldColor           = Colors.COLOR_BS_DARK
    DashboardReportsListSearchQueryFieldBackgroundColor = Colors.COLOR_WHITE
    DashboardReportsListSearchQueryFieldBorderColor     = Colors.COLOR_VSC_LIGHT

    DashboardReportsListCurrentPageColor                = Colors.COLOR_BS_DARK
    DashboardReportsListCurrentPageBackgroundColor      = Colors.COLOR_WHITE
    DashboardReportsListCurrentPageBorderColor          = Colors.COLOR_VSC_LIGHT

    DashboardReportsListTotalPagesColor                 = Colors.COLOR_BS_DARK
    DashboardReportsListTotalPagesBorderColor           = Colors.COLOR_VSC_LIGHT

    DashboardReportsListPagesLabelColor                 = Colors.COLOR_BS_DARK
    DashboardReportsListPagesLabelBorderColor           = Colors.COLOR_VSC_LIGHT

    DashboardReportsListOfPagesLabelColor                 = Colors.COLOR_BS_DARK
    DashboardReportsListOfPagesLabelBorderColor           = Colors.COLOR_VSC_LIGHT

    DashboardReportsListPageControlColor                = Colors.COLOR_BS_DARK
    DashboardReportsListPageControlHoverColor           = Colors.COLOR_BS_DARK
    DashboardReportsListPageControlBackgroundColor      = Colors.COLOR_WHITE
    DashboardReportsListPageControlHoverBackgroundColor = Colors.COLOR_BS_LIGHT
    DashboardReportsListPageControlBorderColor          = Colors.COLOR_VSC_LIGHT

    DashboardReportsListSearchColor                = Colors.COLOR_BS_DARK
    DashboardReportsListSearchHoverColor           = Colors.COLOR_BS_DARK
    DashboardReportsListSearchBackgroundColor      = Colors.COLOR_WHITE
    DashboardReportsListSearchHoverBackgroundColor = Colors.COLOR_BS_LIGHT
    DashboardReportsListSearchBorderColor          = Colors.COLOR_VSC_LIGHT

    DashboardReportsListNewReportColor                = Colors.COLOR_BS_DARK
    DashboardReportsListNewReportHoverColor           = Colors.COLOR_BS_DARK
    DashboardReportsListNewReportBackgroundColor      = Colors.COLOR_WHITE
    DashboardReportsListNewReportHoverBackgroundColor = Colors.COLOR_BS_LIGHT
    DashboardReportsListNewReportBorderColor          = Colors.COLOR_VSC_LIGHT

    DashboardReportCardBackgroundColor        = Colors.COLOR_WHITE
    DashboardReportCardBorderColor            = Colors.COLOR_VSC_LIGHT
    DashboardReportCardHoveredBackgroundColor = Colors.COLOR_BS_LIGHT

    DashboardReportCardTitleColor = Colors.COLOR_BS_DARK
    DashboardReportCardIdColor    = Colors.COLOR_VSC_TERTIARY

    DashboardReportCardPropertyNameColor  = Colors.COLOR_BS_DARK
    DashboardReportCardPropertyValueColor = Colors.COLOR_BS_DARK

    DashboardReportWidgetTitleColor = Colors.COLOR_BS_DARK
    DashboardReportWidgetIdColor    = Colors.COLOR_VSC_TERTIARY

    DashboardReportWidgetPropertyNameColor  = Colors.COLOR_BS_DARK
    DashboardReportWidgetPropertyValueColor = Colors.COLOR_BS_DARK

    DashboardReportWidgetSubtitleColor = Colors.COLOR_BS_DARK

    DashboardReportItemPColor             = Colors.COLOR_BS_DARK
    DashboardReportItemPreBackgroundColor = Colors.COLOR_BS_DARK
    DashboardReportItemPreColor           = Colors.COLOR_WHITE


CurrentTheme = None


def set_theme(theme):
    global CurrentTheme

    if theme == THEME_DARK:
        CurrentTheme = DarkTheme
        return
    
    if theme == THEME_LIGHT:
        CurrentTheme = LightTheme
        return
    
    CurrentTheme = Theme


if sys.platform == 'win32':
    import winreg
    reg = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    )
    value, _ = winreg.QueryValueEx(reg, "AppsUseLightTheme")
    if value == 0:
        set_theme(THEME_DARK)
    else:
        set_theme(THEME_LIGHT)
else:
    set_theme(THEME_DARK)
