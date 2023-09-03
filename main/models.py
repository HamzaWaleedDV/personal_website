from django.db import models

# Create your models here.

ICONS_CHOICES = (
    ("", "Select an icon"),
    ("home", "home"),
    ("user", "user"),
    ("setgs", "setgs"),
    ("search", "search"),
    ("menu", "menu"),
    ("shopping-cart", "shopping-cart"),
    ("calendar", "calendar"),
    ("comment", "comment"),
    ("arrow-up", "arrow-up"),
    ("arrow-down", "arrow-down"),
    ("arrow-left", "arrow-left"),
    ("arrow-right", "arrow-right"),
    ("angle-up", "angle-up"),
    ("angle-down", "angle-down"),
    ("angle-left", "angle-left"),
    ("angle-right", "angle-right"),
    ("angle-double-up", "angle-double-up"),
    ("angle-double-down", "angle-double-down"),
    ("angle-double-left", "angle-double-left"),
    ("angle-double-right", "angle-double-right"),
    ("check", "check"),
    ("close", "close"),
    ("close-circle", "close-circle"),
    ("check-circle", "check-circle"),
    ("check-box", "check-box"),
    ("zoom-in", "zoom-in"),
    ("zoom-out", "zoom-out"),
    ("clip", "clip"),
    ("pencil", "pencil"),
    ("calendar", "calendar"),
    ("e", "e"),
    ("alarm-clock", "alarm-clock"),
    ("notepad", "notepad"),
    ("dashboard", "dashboard"),
    ("announcement", "announcement"),
    ("credit-card", "credit-card"),
    ("link", "link"),
    ("star", "star"),
    ("heart", "heart"),
    ("stats-up", "stats-up"),
    ("stats-down", "stats-down"),
    ("pie-chart", "pie-chart"),
    ("bar-chart", "bar-chart"),
    ("arrow-top-right", "arrow-top-right"),
    ("arrow-top-left", "arrow-top-left"),
    ("arrow-circle-up", "arrow-circle-up"),
    ("arrow-circle-down", "arrow-circle-down"),
    ("arrow-circle-left", "arrow-circle-left"),
    ("arrow-circle-right", "arrow-circle-right"),
    ("angle-up", "angle-up"),
    ("angle-down", "angle-down"),
    ("angle-left", "angle-left"),
    ("angle-right", "angle-right"),
    ("angle-double-up", "angle-double-up"),
    ("angle-double-down", "angle-double-down"),
    ("angle-double-left", "angle-double-left"),
    ("angle-double-right", "angle-double-right"),
    ("help", "help"),
    ("minus", "minus"),
    ("plus", "plus"),
    ("filter", "filter"),
    ("target", "target"),
    ("blackboard", "blackboard"),
    ("upload", "upload"),
    ("download", "download"),
    ("light-bulb", "light-bulb"),
    ("support", "support"),
    ("signal", "signal"),
    ("flag", "flag"),
    ("comments", "comments"),
    ("control-stop", "control-stop"),
    ("control-pause", "control-pause"),
    ("control-play", "control-play"),
    ("control-forward", "control-forward"),
    ("control-backward", "control-backward"),
    ("angle-up", "angle-up"),
    ("angle-down", "angle-down"),
    ("angle-left", "angle-left"),
    ("angle-right", "angle-right"),
    ("angle-double-up", "angle-double-up"),
    ("angle-double-down", "angle-double-down"),
    ("angle-double-left", "angle-double-left"),
    ("angle-double-right", "angle-double-right"),
    ("help", "help"),
    ("minus", "minus"),
    ("plus", "plus"),
    ("filter", "filter"),
    ("target", "target"),
    ("blackboard", "blackboard"),
    ("upload", "upload"),
    ("download", "download"),
    ("light-bulb", "light-bulb"),
    ("support", "support"),
    ("signal", "signal"),
    ("flag", "flag"),
    ("money", "money"),
    ("credit-card", "credit-card"),
    ("calculator", "calculator"),
    ("setgs", "setgs"),
    ("briefcase", "briefcase"),
    ("book", "book"),
    ("ink-pen", "ink-pen"),
    ("pencil", "pencil"),
    ("stamp", "stamp"),
    ("cut", "cut"),
    ("link", "link"),
    ("cloud", "cloud"),
    ("help-alt", "help-alt"),
    ("home", "home"),
    ("direcn", "direcn"),
    ("direcn-alt", "direcn-alt"),
    ("direcns", "direcns"),
    ("announcement", "announcement"),
    ("e", "e"),
    ("alarm-clock", "alarm-clock"),
    ("dashboard", "dashboard"),
    ("control-record", "control-record"),
    ("traffic-cone", "traffic-cone"),
    ("light-bulb", "light-bulb"),
    ("bolt", "bolt"),
    ("wand", "wand"),
    ("rocket", "rocket"),
    ("arrow-up", "arrow-up"),
    ("arrow-down", "arrow-down"),
    ("arrow-left", "arrow-left"),
    ("arrow-right", "arrow-right"),
    ("arrows-veral", "arrows-veral"),
    ("arrows-horizontal", "arrows-horizontal"),
    ("split-v", "split-v"),
    ("split-h", "split-h"),
    ("hand-open", "hand-open"),
    ("hand-open-outline", "hand-open-outline"),
    ("hand-point-up", "hand-point-up"),
    ("hand-point-right", "hand-point-right"),
    ("hand-point-left", "hand-point-left"),
    ("hand-point-down", "hand-point-down"),
    ("back-right", "back-right"),
    ("back-left", "back-left"),
    ("exchange-veral", "exchange-veral"),
    ("exchange", "exchange"),
    ("ket", "ket"),
    ("layout", "layout"),
    ("layout-sidebar-left", "layout-sidebar-left"),
    ("layout-sidebar-right", "layout-sidebar-right"),
    ("layout-sidebar-none", "layout-sidebar-none"),
    ("layout-cta-left", "layout-cta-left"),
    ("layout-cta-right", "layout-cta-right"),
    ("layout-footer", "layout-footer"),
    ("layout-subheader", "layout-subheader"),
    ("layout-menu", "layout-menu"),
    ("layout-menu-v", "layout-menu-v"),
    ("layout-bullets", "layout-bullets"),
    ("layout-horizontal", "layout-horizontal"),
    ("layout-horizontal-2", "layout-horizontal-2"),
    ("layout-veral", "layout-veral"),
    ("fullscreen", "fullscreen"),
    ("ruler", "ruler"),
    ("ruler-alt", "ruler-alt"),
    ("browser", "browser"),
    ("widgeed", "widgeed"),
    ("widget", "widget"),
    ("widget-alt", "widget-alt"),
    ("widget-ized", "widget-ized"),
    ("wand", "wand"),
    ("save", "save"),
    ("save-alt", "save-alt"),
    ("anchor", "anchor"),
    ("stack-overflow", "stack-overflow"),
    ("underline", "underline"),
    ("paragraph", "paragraph"),
    ("align-left", "align-left"),
    ("align-center", "align-center"),
    ("align-right", "align-right"),
    ("align-jusy", "align-jusy"),
    ("list", "list"),
    ("text", "text"),
    ("text-width", "text-width"),
    ("text-height", "text-height"),
    ("italic", "italic"),
    ("bold", "bold"),
    ("arrow-top-right", "arrow-top-right"),
    ("arrow-top-left", "arrow-top-left"),
    ("arrow-circle-up", "arrow-circle-up"),
    ("arrow-circle-down", "arrow-circle-down"),
    ("arrow-circle-left", "arrow-circle-left"),
    ("arrow-circle-right", "arrow-circle-right"),
    ("arrow-up", "arrow-up"),
    ("arrow-down", "arrow-down"),
    ("arrow-left", "arrow-left"),
    ("arrow-right", "arrow-right"),
    ("arrow-right-up", "arrow-right-up"),
    ("arrow-left-up", "arrow-left-up"),
    ("arrow-right-down", "arrow-right-down"),
    ("arrow-left-down", "arrow-left-down"),
    ("desktop", "desktop"),
    ("crown", "crown"),
    ("bar-chart", "bar-chart"),
)


class Personal(models.Model):
    name = models.CharField(max_length=30)
    career = models.CharField(max_length=80)
    personal_photo = models.ImageField()
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "People"

class Logo(models.Model):
    title = models.CharField(max_length=30, default="My Logo")
    logo = models.ImageField()

    def __str__(self):
        return self.title

class CV(models.Model):  
    title = models.CharField(max_length=30, default="My CV")
    cv = models.FileField()

    def __str__(self):
        return self.title

class Url(models.Model):
    title = models.CharField(max_length=30, default="My Urls")
    url = models.URLField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    my_skills = models.CharField(max_length=50)
    desc_for_pic = models.CharField(
        max_length=50,
        choices=sorted(ICONS_CHOICES),
        default="Select an icon",
    )
    precent_finish = models.CharField(max_length=10, default="80%")

    def __str__(self):
        return self.my_skills


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    url = models.URLField()
    image_for_project = models.ImageField()

    def __str__(self):
        return self.title
    

class Facts(models.Model):
    title = models.CharField(max_length=20)
    number = models.IntegerField()

    class Meta:
        verbose_name = "fact"
        verbose_name_plural = "facts"