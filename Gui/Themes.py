
import sys
import datetime

from Gui import Colors
from Gui import Fonts

THEME_DEFAULT = 'Default'
THEME_DARK = 'Dark'
THEME_LIGHT = 'Light'


class Theme:
    NAME = THEME_DEFAULT

    SplitterBackgroundColor = Colors.COLOR_VSC_TERTIARY

    ScrollHorizontalBackgroundColor       = Colors.COLOR_VSC_SECONDARY
    ScrollHorizontalHandleBackgroundColor = Colors.COLOR_VSC_LIGHT
    ScrollHorizontalBorderColor           = Colors.COLOR_VSC_TERTIARY
    ScrollHorizontalBorderRadius          = 0
    ScrollHorizontalHandleBorderRadius    = 0
    ScrollHorizontalMinWidth              = 128
    ScrollHorizontalHeight                = 20
    ScrollVerticalBackgroundColor         = Colors.COLOR_VSC_SECONDARY
    ScrollVerticalHandleBackgroundColor   = Colors.COLOR_VSC_LIGHT
    ScrollVerticalBorderColor             = Colors.COLOR_VSC_TERTIARY
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

    WelcomeLogoFont       = Fonts.FONT_BLENDER_PRO_BOLD
    WelcomeLogoFontWeight = Fonts.Font.Bold
    WelcomeLogoFontSize   = 64
    WelcomeLogoColor      = Colors.COLOR_BS_LIGHT

    WelcomeOpenProjectFont       = Fonts.FONT_BLENDER_PRO_BOLD
    WelcomeOpenProjectFontWeight = Fonts.Font.Bold
    WelcomeOpenProjectFontSize   = 24
    WelcomeOpenProjectColor      = Colors.COLOR_BS_LIGHT

    DashboardScreenBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBorderColor     = Colors.COLOR_VSC_TERTIARY
    DashboardBodyBackgroundColor   = Colors.COLOR_VSC_PRIMARY
    DashboardBodyBorderColor       = Colors.COLOR_VSC_TERTIARY
    DashboardFooterBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBorderColor     = Colors.COLOR_VSC_TERTIARY

    DashboardReloadProjectFont                 = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReloadProjectFontWeight           = Fonts.Font.Bold
    DashboardReloadProjectFontSize             = 18
    DashboardReloadProjectColor                = Colors.COLOR_VSC_LIGHT
    DashboardReloadProjectHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardReloadProjectBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    DashboardReloadProjectHoverBackgroundColor = Colors.COLOR_VSC_TERTIARY
    DashboardReloadProjectBorderColor          = Colors.COLOR_VSC_SECONDARY

    DashboardSwitchThemeFont                 = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardSwitchThemeFontWeight           = Fonts.Font.Bold
    DashboardSwitchThemeFontSize             = 18
    DashboardSwitchThemeColor                = Colors.COLOR_VSC_LIGHT
    DashboardSwitchThemeHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardSwitchThemeBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    DashboardSwitchThemeHoverBackgroundColor = Colors.COLOR_VSC_TERTIARY
    DashboardSwitchThemeBorderColor          = Colors.COLOR_VSC_SECONDARY

    DashboardReportsListSectionBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportSectionBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    
    DashboardNoReportSelectedFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardNoReportSelectedFontWeight = Fonts.Font.Bold
    DashboardNoReportSelectedFontSize   = 20
    DashboardNoReportSelectedColor      = Colors.COLOR_VSC_LIGHT

    DashboardNoReportsFoundFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardNoReportsFoundFontWeight = Fonts.Font.Bold
    DashboardNoReportsFoundFontSize   = 20
    DashboardNoReportsFoundColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportsListToolsBorderColor = Colors.COLOR_VSC_TERTIARY

    DashboardReportsListSearchQueryFieldFont            = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportsListSearchQueryFieldFontWeight      = Fonts.Font.Bold
    DashboardReportsListSearchQueryFieldFontSize        = 16
    DashboardReportsListSearchQueryFieldColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListSearchQueryFieldBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListSearchQueryFieldBorderColor     = Colors.COLOR_VSC_TERTIARY

    DashboardReportsListSearchFont                 = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportsListSearchFontWeight           = Fonts.Font.Bold
    DashboardReportsListSearchFontSize             = 16
    DashboardReportsListSearchColor                = Colors.COLOR_VSC_LIGHT
    DashboardReportsListSearchHoverColor           = Colors.COLOR_VSC_LIGHT
    DashboardReportsListSearchBackgroundColor      = Colors.COLOR_VSC_PRIMARY
    DashboardReportsListSearchHoverBackgroundColor = Colors.COLOR_VSC_SECONDARY
    DashboardReportsListSearchBorderColor          = Colors.COLOR_VSC_TERTIARY

    DashboardReportCardBackgroundColor        = Colors.COLOR_VSC_PRIMARY
    DashboardReportCardBorderColor            = Colors.COLOR_VSC_TERTIARY
    DashboardReportCardHoveredBackgroundColor = Colors.COLOR_VSC_SECONDARY

    DashboardReportCardTitleFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportCardTitleFontWeight = Fonts.Font.Bold
    DashboardReportCardTitleFontSize   = 14
    DashboardReportCardTitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportCardIdFont       = Fonts.FONT_BLENDER_PRO_THIN
    DashboardReportCardIdFontWeight = Fonts.Font.Thin
    DashboardReportCardIdFontSize   = 12
    DashboardReportCardIdColor      = Colors.COLOR_VSC_QUATERNARY

    DashboardReportCardPropertyNameFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportCardPropertyNameFontWeight = Fonts.Font.Bold
    DashboardReportCardPropertyNameFontSize   = 14
    DashboardReportCardPropertyNameColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportCardPropertyValueFont       = Fonts.FONT_BLENDER_PRO_THIN
    DashboardReportCardPropertyValueFontWeight = Fonts.Font.Thin
    DashboardReportCardPropertyValueFontSize   = 14
    DashboardReportCardPropertyValueColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetMargins = (64, 32, 64, 32)

    DashboardReportWidgetTitleFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportWidgetTitleFontWeight = Fonts.Font.Bold
    DashboardReportWidgetTitleFontSize   = 18
    DashboardReportWidgetTitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetIdFont       = Fonts.FONT_BLENDER_PRO_THIN
    DashboardReportWidgetIdFontWeight = Fonts.Font.Thin
    DashboardReportWidgetIdFontSize   = 14
    DashboardReportWidgetIdColor      = Colors.COLOR_VSC_QUATERNARY

    DashboardReportWidgetPropertyNameFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportWidgetPropertyNameFontWeight = Fonts.Font.Bold
    DashboardReportWidgetPropertyNameFontSize   = 14
    DashboardReportWidgetPropertyNameColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetPropertyValueFont       = Fonts.FONT_BLENDER_PRO_THIN
    DashboardReportWidgetPropertyValueFontWeight = Fonts.Font.Thin
    DashboardReportWidgetPropertyValueFontSize   = 14
    DashboardReportWidgetPropertyValueColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportWidgetSubtitleFont       = Fonts.FONT_BLENDER_PRO_BOLD
    DashboardReportWidgetSubtitleFontWeight = Fonts.Font.Bold
    DashboardReportWidgetSubtitleFontSize   = 16
    DashboardReportWidgetSubtitleColor      = Colors.COLOR_VSC_LIGHT

    DashboardReportItemPFont       = Fonts.FONT_BLENDER_PRO_BOOK
    DashboardReportItemPFontWeight = Fonts.Font.Regular
    DashboardReportItemPFontSize   = 14
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

    DashboardReportsListSearchColor                = Colors.COLOR_BS_DARK
    DashboardReportsListSearchHoverColor           = Colors.COLOR_BS_DARK
    DashboardReportsListSearchBackgroundColor      = Colors.COLOR_WHITE
    DashboardReportsListSearchHoverBackgroundColor = Colors.COLOR_BS_LIGHT
    DashboardReportsListSearchBorderColor          = Colors.COLOR_VSC_LIGHT

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


# if sys.platform == 'win32':
#     import winreg
#     reg = winreg.OpenKey(
#         winreg.HKEY_CURRENT_USER,
#         r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
#     )
#     value, _ = winreg.QueryValueEx(reg, "AppsUseLightTheme")
#     if value == 0:
#         set_theme(THEME_DARK)
#     else:
#         set_theme(THEME_LIGHT)
# else:
#     set_theme(THEME_DARK)

if 6 <= datetime.datetime.now().hour < 19:
    set_theme(THEME_LIGHT)
else:
    set_theme(THEME_DARK)
