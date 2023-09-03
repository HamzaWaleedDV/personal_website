# Generated by Django 4.2.4 on 2023-09-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_skills_precent_finish_alter_skills_desc_for_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='desc_for_pic',
            field=models.CharField(choices=[('', 'Select an icon'), ('alarm-clock', 'alarm-clock'), ('alarm-clock', 'alarm-clock'), ('align-center', 'align-center'), ('align-jusy', 'align-jusy'), ('align-left', 'align-left'), ('align-right', 'align-right'), ('anchor', 'anchor'), ('angle-double-down', 'angle-double-down'), ('angle-double-down', 'angle-double-down'), ('angle-double-down', 'angle-double-down'), ('angle-double-left', 'angle-double-left'), ('angle-double-left', 'angle-double-left'), ('angle-double-left', 'angle-double-left'), ('angle-double-right', 'angle-double-right'), ('angle-double-right', 'angle-double-right'), ('angle-double-right', 'angle-double-right'), ('angle-double-up', 'angle-double-up'), ('angle-double-up', 'angle-double-up'), ('angle-double-up', 'angle-double-up'), ('angle-down', 'angle-down'), ('angle-down', 'angle-down'), ('angle-down', 'angle-down'), ('angle-left', 'angle-left'), ('angle-left', 'angle-left'), ('angle-left', 'angle-left'), ('angle-right', 'angle-right'), ('angle-right', 'angle-right'), ('angle-right', 'angle-right'), ('angle-up', 'angle-up'), ('angle-up', 'angle-up'), ('angle-up', 'angle-up'), ('announcement', 'announcement'), ('announcement', 'announcement'), ('arrow-circle-down', 'arrow-circle-down'), ('arrow-circle-down', 'arrow-circle-down'), ('arrow-circle-left', 'arrow-circle-left'), ('arrow-circle-left', 'arrow-circle-left'), ('arrow-circle-right', 'arrow-circle-right'), ('arrow-circle-right', 'arrow-circle-right'), ('arrow-circle-up', 'arrow-circle-up'), ('arrow-circle-up', 'arrow-circle-up'), ('arrow-down', 'arrow-down'), ('arrow-down', 'arrow-down'), ('arrow-down', 'arrow-down'), ('arrow-left', 'arrow-left'), ('arrow-left', 'arrow-left'), ('arrow-left', 'arrow-left'), ('arrow-left-down', 'arrow-left-down'), ('arrow-left-up', 'arrow-left-up'), ('arrow-right', 'arrow-right'), ('arrow-right', 'arrow-right'), ('arrow-right', 'arrow-right'), ('arrow-right-down', 'arrow-right-down'), ('arrow-right-up', 'arrow-right-up'), ('arrow-top-left', 'arrow-top-left'), ('arrow-top-left', 'arrow-top-left'), ('arrow-top-right', 'arrow-top-right'), ('arrow-top-right', 'arrow-top-right'), ('arrow-up', 'arrow-up'), ('arrow-up', 'arrow-up'), ('arrow-up', 'arrow-up'), ('arrows-horizontal', 'arrows-horizontal'), ('arrows-veral', 'arrows-veral'), ('back-left', 'back-left'), ('back-right', 'back-right'), ('bar-chart', 'bar-chart'), ('bar-chart', 'bar-chart'), ('blackboard', 'blackboard'), ('blackboard', 'blackboard'), ('bold', 'bold'), ('bolt', 'bolt'), ('book', 'book'), ('briefcase', 'briefcase'), ('browser', 'browser'), ('calculator', 'calculator'), ('calendar', 'calendar'), ('calendar', 'calendar'), ('check', 'check'), ('check-box', 'check-box'), ('check-circle', 'check-circle'), ('clip', 'clip'), ('close', 'close'), ('close-circle', 'close-circle'), ('cloud', 'cloud'), ('comment', 'comment'), ('comments', 'comments'), ('control-backward', 'control-backward'), ('control-forward', 'control-forward'), ('control-pause', 'control-pause'), ('control-play', 'control-play'), ('control-record', 'control-record'), ('control-stop', 'control-stop'), ('credit-card', 'credit-card'), ('credit-card', 'credit-card'), ('crown', 'crown'), ('cut', 'cut'), ('dashboard', 'dashboard'), ('dashboard', 'dashboard'), ('desktop', 'desktop'), ('direcn', 'direcn'), ('direcn-alt', 'direcn-alt'), ('direcns', 'direcns'), ('download', 'download'), ('download', 'download'), ('e', 'e'), ('e', 'e'), ('exchange', 'exchange'), ('exchange-veral', 'exchange-veral'), ('filter', 'filter'), ('filter', 'filter'), ('flag', 'flag'), ('flag', 'flag'), ('fullscreen', 'fullscreen'), ('hand-open', 'hand-open'), ('hand-open-outline', 'hand-open-outline'), ('hand-point-down', 'hand-point-down'), ('hand-point-left', 'hand-point-left'), ('hand-point-right', 'hand-point-right'), ('hand-point-up', 'hand-point-up'), ('heart', 'heart'), ('help', 'help'), ('help', 'help'), ('help-alt', 'help-alt'), ('home', 'home'), ('home', 'home'), ('ink-pen', 'ink-pen'), ('italic', 'italic'), ('ket', 'ket'), ('layout', 'layout'), ('layout-bullets', 'layout-bullets'), ('layout-cta-left', 'layout-cta-left'), ('layout-cta-right', 'layout-cta-right'), ('layout-footer', 'layout-footer'), ('layout-horizontal', 'layout-horizontal'), ('layout-horizontal-2', 'layout-horizontal-2'), ('layout-menu', 'layout-menu'), ('layout-menu-v', 'layout-menu-v'), ('layout-sidebar-left', 'layout-sidebar-left'), ('layout-sidebar-none', 'layout-sidebar-none'), ('layout-sidebar-right', 'layout-sidebar-right'), ('layout-subheader', 'layout-subheader'), ('layout-veral', 'layout-veral'), ('light-bulb', 'light-bulb'), ('light-bulb', 'light-bulb'), ('light-bulb', 'light-bulb'), ('link', 'link'), ('link', 'link'), ('list', 'list'), ('menu', 'menu'), ('minus', 'minus'), ('minus', 'minus'), ('money', 'money'), ('notepad', 'notepad'), ('paragraph', 'paragraph'), ('pencil', 'pencil'), ('pencil', 'pencil'), ('pie-chart', 'pie-chart'), ('plus', 'plus'), ('plus', 'plus'), ('rocket', 'rocket'), ('ruler', 'ruler'), ('ruler-alt', 'ruler-alt'), ('save', 'save'), ('save-alt', 'save-alt'), ('search', 'search'), ('setgs', 'setgs'), ('setgs', 'setgs'), ('shopping-cart', 'shopping-cart'), ('signal', 'signal'), ('signal', 'signal'), ('split-h', 'split-h'), ('split-v', 'split-v'), ('stack-overflow', 'stack-overflow'), ('stamp', 'stamp'), ('star', 'star'), ('stats-down', 'stats-down'), ('stats-up', 'stats-up'), ('support', 'support'), ('support', 'support'), ('target', 'target'), ('target', 'target'), ('text', 'text'), ('text-height', 'text-height'), ('text-width', 'text-width'), ('traffic-cone', 'traffic-cone'), ('underline', 'underline'), ('upload', 'upload'), ('upload', 'upload'), ('user', 'user'), ('wand', 'wand'), ('wand', 'wand'), ('widgeed', 'widgeed'), ('widget', 'widget'), ('widget-alt', 'widget-alt'), ('widget-ized', 'widget-ized'), ('zoom-in', 'zoom-in'), ('zoom-out', 'zoom-out')], default='Select an icon', max_length=50),
        ),
    ]
