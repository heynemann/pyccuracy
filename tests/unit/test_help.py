from pyccuracy.help import LanguageViewer

url_regex = r"(?P<url>[\"](([\w:/._-]|\=|\?|\&|\"|\;|\%)+)[\"]|([\w\s_.-]+))$"

def test_get_action():
    viewer = LanguageViewer(language='en-us')
    action = viewer.get_actions('select_does_not_have_selected_value')
    assert 'select_does_not_have_selected_value' in action
    assert action.get('select_does_not_have_selected_value') == '(And )I see "select_name" select does not have selected value of "value"'
    
    viewer = LanguageViewer(language='pt-br')
    action = viewer.get_actions('select_does_not_have_selected_value')
    assert 'select_does_not_have_selected_value' in action
    assert action.get('select_does_not_have_selected_value') == '(E )[eE]u vejo que o valor selecionado da select "select_name" não é "value"'

def test_make_regex_readable_for_pt_br():
    viewer = LanguageViewer()
    
    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a imagem [\"](?P<image_name>.+)[\"] tem src de [\"](?P<src>.+)[\"]$')\
            == '(E )[eE]u vejo que a imagem "image_name" tem src de "src"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a radio [\"](?P<radio_key>.+)[\"] está desmarcada$')\
            == '(E )[eE]u vejo que a radio "radio_key" está desmarcada'

    assert viewer.make_it_readable(r'^(E )?[eE]u preencho a caixa de texto [\"](?P<textbox_name>.+)[\"] com [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u preencho a caixa de texto "textbox_name" com "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u espero por (?P<timeout>\d+([.]\d+)?) segundo[s]?$')\
            == '(E )[eE]u espero por [X|X.X] segundo[s]'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o link [\"](?P<link_name>.+)[\"] tem href [\"](?P<href>.+)[\"]$')\
            == '(E )[eE]u vejo que o link "link_name" tem href "href"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o índice selecionado da select [\"](?P<select_name>.+)[\"] é (?P<index>\d+)$')\
            == '(E )[eE]u vejo que o índice selecionado da select "select_name" é X'

    assert viewer.make_it_readable(r'^(E )?[eE]u retiro o mouse d[oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"]$')\
            == '(E )[eE]u retiro o mouse d[oa] [element_type|element selector] "element_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a página atual contém [\"\'](?P<expected_markup>.+)[\'\"]$')\
            == '(E )[eE]u vejo que a página atual contém "expected_markup"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a checkbox [\"](?P<checkbox_key>.+)[\"] está marcada$')\
            == '(E )[eE]u vejo que a checkbox "checkbox_key" está marcada'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a página atual não contém [\"\'](?P<expected_markup>.+)[\'\"]$')\
            == '(E )[eE]u vejo que a página atual não contém "expected_markup"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a caixa de texto [\"](.+)[\"] não contém [\"](.+)[\"]$')\
            == '(E )[eE]u vejo que a caixa de texto "blah" não contém "blah"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a select [\"](?P<select_name>.+)[\"] contém uma opção com texto [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que a select "select_name" contém uma opção com texto "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u passo o mouse n[oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"]$')\
            == '(E )[eE]u passo o mouse n[oa] [element_type|element selector] "element_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [ao] (?P<element_type><element selector>) [\"](?P<element_name>.+)[\"] contém o estilo [\"](?P<style_name>.+)[\"]$')\
            == '(E )[eE]u vejo que [ao] [element_type|element selector] "element_name" contém o estilo "style_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o valor selecionado da select [\"](?P<select_name>.+)[\"] é [\"](?P<option_value>.+)[\"]$')\
            == '(E )[eE]u vejo que o valor selecionado da select "select_name" é "option_value"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] está habilitad[oa]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" está habilitad[oa]'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] contém exatamente o markup [\"](?P<markup>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" contém exatamente o markup "markup"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"]$')\
            == '(E )[eE]u vejo [oa] [element_type|element selector] "element_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] não contém o markup [\"](?P<markup>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" não contém o markup "markup"'

    assert viewer.make_it_readable(r'^(E )?[eE]u seleciono o item com índice (?P<index>\d+) na select [\"](?P<select_name>.+)[\"]$')\
            == '(E )[eE]u seleciono o item com índice X na select "select_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u estou n[oa] %s' % url_regex)\
            == '(E )[eE]u estou n[oa] [page|"url"]', "result was: %s" % viewer.make_it_readable(r'^(E )?[eE]u estou n[oa] %s' % url_regex)

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a radio [\"](?P<radio_key>.+)[\"] está marcada$')\
            == '(E )[eE]u vejo que a radio "radio_key" está marcada'

    assert viewer.make_it_readable(r'^(E )?[eE]u marco a checkbox [\"](?P<checkbox_key>.+)[\"]$')\
            == '(E )[eE]u marco a checkbox "checkbox_key"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a caixa de texto [\"](?P<textbox_name>.+)[\"] está vazia$')\
            == '(E )[eE]u vejo que a caixa de texto "textbox_name" está vazia'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a caixa de texto [\"](.+)[\"] não contém exatamente [\"](.+)[\"]$')\
            == '(E )[eE]u vejo que a caixa de texto "blah" não contém exatamente "blah"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] não contém exatamente [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" não contém exatamente "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a imagem [\"](?P<image_name>.+)[\"] não tem src de [\"](?P<src>.+)[\"]$')\
            == '(E )[eE]u vejo que a imagem "image_name" não tem src de "src"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] não contém [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" não contém "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u marco a radio [\"](?P<radio_key>.+)[\"]$')\
            == '(E )[eE]u marco a radio "radio_key"'

    assert viewer.make_it_readable(r'^(E )?[eE]u seleciono o item com valor [\"](?P<option_value>.+)[\"] na select [\"](?P<select_name>.+)[\"]$')\
            == '(E )[eE]u seleciono o item com valor "option_value" na select "select_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] contém o markup [\"](?P<markup>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" contém o markup "markup"'

    assert viewer.make_it_readable(r'^(E )?[eE]u seleciono o item com texto [\"](?P<text>.+)[\"] na select [\"](?P<select_name>.+)[\"]$')\
            == '(E )[eE]u seleciono o item com texto "text" na select "select_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo o título [\"](?P<title>.+)[\"]$')\
            == '(E )[eE]u vejo o título "title"'

    assert viewer.make_it_readable(r'^(E )?[eE]u não vejo [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"]$')\
            == '(E )[eE]u não vejo [oa] [element_type|element selector] "element_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a select [\"](?P<select_name>.+)[\"] não contém uma opção com texto [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que a select "select_name" não contém uma opção com texto "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o índice selecionado da select [\"](?P<select_name>.+)[\"] não é (?P<index>\d+)$')\
            == '(E )[eE]u vejo que o índice selecionado da select "select_name" não é X'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a checkbox [\"](?P<checkbox_key>.+)[\"] está desmarcada$')\
            == '(E )[eE]u vejo que a checkbox "checkbox_key" está desmarcada'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [ao] (?P<element_type><element selector>) [\"](?P<element_name>.+)[\"] não contém o estilo [\"](?P<style_name>.+)[\"]$')\
            == '(E )[eE]u vejo que [ao] [element_type|element selector] "element_name" não contém o estilo "style_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o link [\"](?P<link_name>.+)[\"] tem texto [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que o link "link_name" tem texto "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u desmarco a checkbox [\"](?P<checkbox_key>.+)[\"]$')\
            == '(E )[eE]u desmarco a checkbox "checkbox_key"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] contém exatamente [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" contém exatamente "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] não contém exatamente o markup [\"](?P<markup>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" não contém exatamente o markup "markup"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a caixa de texto [\"](?P<textbox_name>.+)[\"] não está vazia$')\
            == '(E )[eE]u vejo que a caixa de texto "textbox_name" não está vazia'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] está desabilitad[oa]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" está desabilitad[oa]'

    assert viewer.make_it_readable(r'^(E )?[eE]u espero [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] desaparecer( por (?P<timeout>\d+) segundos)?$')\
            == '(E )[eE]u espero [oa] [element_type|element selector] "element_name" desaparecer( por X segundos)'

    assert viewer.make_it_readable(r'^(E )?[eE]u espero [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] aparecer( por (?P<timeout>\d+) segundos)?$')\
            == '(E )[eE]u espero [oa] [element_type|element selector] "element_name" aparecer( por X segundos)'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a caixa de texto [\"](.+)[\"] contém exatamente [\"](.+)[\"]$')\
            == '(E )[eE]u vejo que a caixa de texto "blah" contém exatamente "blah"'

    assert viewer.make_it_readable(r'^(E )?[eE]u espero a página ser carregada(?P<timeout> por (\d+) segundos)?$')\
            == '(E )[eE]u espero a página ser carregada( por X segundos)', "result was: %s" % viewer.make_it_readable(r'^(E )?[eE]u espero a página ser carregada(?P<timeout> por (\d+) segundos)?$')

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o texto selecionado da select [\"](?P<select_name>.+)[\"] não é [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que o texto selecionado da select "select_name" não é "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que a caixa de texto [\"](.+)[\"] contém [\"](.+)[\"]$')\
            == '(E )[eE]u vejo que a caixa de texto "blah" contém "blah"'

    assert viewer.make_it_readable(r'^(E )?[eE]u preencho lentamente a caixa de texto [\"](?P<textbox_name>.+)[\"] com [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u preencho lentamente a caixa de texto "textbox_name" com "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o texto selecionado da select [\"](?P<select_name>.+)[\"] é [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que o texto selecionado da select "select_name" é "text"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que o valor selecionado da select [\"](?P<select_name>.+)[\"] não é [\"](?P<value>.+)[\"]$')\
            == '(E )[eE]u vejo que o valor selecionado da select "select_name" não é "value"'

    assert viewer.make_it_readable(r'^(E )?[eE]u limpo a caixa de texto [\"](?P<textbox_name>.+)[\"]$')\
            == '(E )[eE]u limpo a caixa de texto "textbox_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u clico n[oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"](?P<should_wait> e espero)?$')\
            == '(E )[eE]u clico n[oa] [element_type|element selector] "element_name"( e espero)'

    assert viewer.make_it_readable(r'^(E )?[eE]u navego para %s' % url_regex)\
            == '(E )[eE]u navego para [page|"url"]'

    assert viewer.make_it_readable(r'^(E )?[eE]u arrasto [oa] (?P<from_element_type><element selector>) [\"](?P<from_element_name>.+)[\"] para [oa] (?P<to_element_type><element selector>) [\"](?P<to_element_name>[^"]+)[\"]?$')\
            == '(E )[eE]u arrasto [oa] [from_element_type|element selector] "from_element_name" para [oa] [to_element_type|element selector] "to_element_name"'

    assert viewer.make_it_readable(r'^(E )?[eE]u vejo que [oa] (?P<element_type><element selector>) [\"](?P<element_name>[^"]+)[\"] contém [\"](?P<text>.+)[\"]$')\
            == '(E )[eE]u vejo que [oa] [element_type|element selector] "element_name" contém "text"'

def test_make_regex_readable_for_en_us():
    viewer = LanguageViewer()

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<image_name>.+)[\"] image has src of [\"](?P<src>.+)[\"]$')\
            == '(And )I see "image_name" image has src of "src"'

    assert viewer.make_it_readable(r'^(And )?I see the [\"](?P<radio_key>.+)[\"] radio is not checked$')\
            == '(And )I see the "radio_key" radio is not checked'

    assert viewer.make_it_readable(r'^(And )?I fill [\"](?P<textbox_name>.+)[\"] textbox with [\"](?P<text>.+)[\"]$')\
            == '(And )I fill "textbox_name" textbox with "text"'

    assert viewer.make_it_readable(r'^(And )?I wait for (?P<timeout>\d+([.]\d+)?) second[s]?$')\
            == '(And )I wait for [X|X.X] second[s]', "result was: %s" % viewer.make_it_readable(r'^(And )?I wait for (?P<timeout>\d+([.]d+)?) second[s]?$')

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<link_name>.+)[\"] link has [\"](?P<href>.+)[\"] href$')\
            == '(And )I see "link_name" link has "href" href'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select has selected index of (?P<index>\d+)$')\
            == '(And )I see "select_name" select has selected index of X'

    assert viewer.make_it_readable(r'^(And )?I mouseout [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>)$')\
            == '(And )I mouseout "element_name" [element_type|element selector]'

    assert viewer.make_it_readable(r'^(And )?I see that current page contains [\"\'](?P<expected_markup>.+)[\'\"]$')\
            == '(And )I see that current page contains "expected_markup"'

    assert viewer.make_it_readable(r'^(And )?I see the [\"](?P<checkbox_key>.+)[\"] checkbox is checked$')\
            == '(And )I see the "checkbox_key" checkbox is checked'

    assert viewer.make_it_readable(r'^(And )?I see that current page does not contain [\"\'](?P<expected_markup>.+)[\'\"]$')\
            == '(And )I see that current page does not contain "expected_markup"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](.+)[\"] textbox does not contain [\"](.+)[\"]$')\
            == '(And )I see "blah" textbox does not contain "blah"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select contains an option with text [\"](?P<text>.+)[\"]$')\
            == '(And )I see "select_name" select contains an option with text "text"'

    assert viewer.make_it_readable(r'^(And )?I mouseover [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>)$')\
            == '(And )I mouseover "element_name" [element_type|element selector]'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>.+)[\"] (?P<element_type><element selector>) has [\"](?P<style_name>.+)[\"] style$')\
            == '(And )I see "element_name" [element_type|element selector] has "style_name" style'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select has selected value of [\"](?P<option_value>.+)[\"]$')\
            == '(And )I see "select_name" select has selected value of "option_value"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) is enabled$')\
            == '(And )I see "element_name" [element_type|element selector] is enabled'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) matches [\"](?P<markup>.+)[\"] markup$')\
            == '(And )I see "element_name" [element_type|element selector] matches "markup" markup'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>.+)[\"] (?P<element_type><element selector>)$')\
            == '(And )I see "element_name" [element_type|element selector]'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) does not contain [\"](?P<markup>.+)[\"] markup$')\
            == '(And )I see "element_name" [element_type|element selector] does not contain "markup" markup'

    assert viewer.make_it_readable(r'^(And )?I select the option with index of (?P<index>\d+) in [\"](?P<select_name>.+)[\"] select$')\
            == '(And )I select the option with index of X in "select_name" select'

    assert viewer.make_it_readable(r'^(And )?I am in the %s' % url_regex)\
            == '(And )I am in the [page|"url"]'

    assert viewer.make_it_readable(r'^(And )?I see the [\"](?P<radio_key>.+)[\"] radio is checked$')\
            == '(And )I see the "radio_key" radio is checked'

    assert viewer.make_it_readable(r'^(And )?I check the [\"](?P<checkbox_key>.+)[\"] checkbox$')\
            == '(And )I check the "checkbox_key" checkbox'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<textbox_name>.+)[\"] textbox is empty$')\
            == '(And )I see "textbox_name" textbox is empty'

    assert viewer.make_it_readable(r'^(And )?I see [\"](.+)[\"] textbox does not match [\"](.+)[\"]$')\
            == '(And )I see "blah" textbox does not match "blah"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) does not match [\"](?P<text>.+)[\"]$')\
            == '(And )I see "element_name" [element_type|element selector] does not match "text"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<image_name>.+)[\"] image does not have src of [\"](?P<src>.+)[\"]$')\
            == '(And )I see "image_name" image does not have src of "src"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) does not contain [\"](?P<text>.+)[\"]$')\
            == '(And )I see "element_name" [element_type|element selector] does not contain "text"'

    assert viewer.make_it_readable(r'^(And )?I check the [\"](?P<radio_key>.+)[\"] radio$')\
            == '(And )I check the "radio_key" radio'

    assert viewer.make_it_readable(r'^(And )?I select the option with value of [\"](?P<option_value>.+)[\"] in [\"](?P<select_name>.+)[\"] select$')\
            == '(And )I select the option with value of "option_value" in "select_name" select'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) contains [\"](?P<markup>.+)[\"] markup$')\
            == '(And )I see "element_name" [element_type|element selector] contains "markup" markup'

    assert viewer.make_it_readable(r'^(And )?I select the option with text of [\"](?P<text>.+)[\"] in [\"](?P<select_name>.+)[\"] select$')\
            == '(And )I select the option with text of "text" in "select_name" select'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<title>.+)[\"] title$')\
            == '(And )I see "title" title'

    assert viewer.make_it_readable(r'^(And )?I do not see [\"](?P<element_name>.+)[\"] (?P<element_type><element selector>)$')\
            == '(And )I do not see "element_name" [element_type|element selector]'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select does not contain an option with text [\"](?P<text>.+)[\"]$')\
            == '(And )I see "select_name" select does not contain an option with text "text"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select does not have selected index of (?P<index>\d+)$')\
            == '(And )I see "select_name" select does not have selected index of X'

    assert viewer.make_it_readable(r'^(And )?I see the [\"](?P<checkbox_key>.+)[\"] checkbox is not checked$')\
            == '(And )I see the "checkbox_key" checkbox is not checked'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>.+)[\"] (?P<element_type><element selector>) does not have [\"](?P<style_name>.+)[\"] style$')\
            == '(And )I see "element_name" [element_type|element selector] does not have "style_name" style'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<link_name>.+)[\"] link has [\"](?P<text>.+)[\"] text$')\
            == '(And )I see "link_name" link has "text" text'

    assert viewer.make_it_readable(r'^(And )?I uncheck the [\"](?P<checkbox_key>.+)[\"] checkbox$')\
            == '(And )I uncheck the "checkbox_key" checkbox'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) matches [\"](?P<text>.+)[\"]$')\
            == '(And )I see "element_name" [element_type|element selector] matches "text"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) does not match [\"](?P<markup>.+)[\"] markup$')\
            == '(And )I see "element_name" [element_type|element selector] does not match "markup" markup'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<textbox_name>.+)[\"] textbox is not empty$')\
            == '(And )I see "textbox_name" textbox is not empty'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) is disabled$')\
            == '(And )I see "element_name" [element_type|element selector] is disabled'

    assert viewer.make_it_readable(r'^(And )?I wait for [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) to disappear( for (?P<timeout>\d+) seconds)?$')\
            == '(And )I wait for "element_name" [element_type|element selector] to disappear( for X seconds)'

    assert viewer.make_it_readable(r'^(And )?I wait for [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) to be present( for (?P<timeout>\d+) seconds)?$')\
            == '(And )I wait for "element_name" [element_type|element selector] to be present( for X seconds)', "result was: %s" % viewer.make_it_readable(r'^(And )?I wait for [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) to be present( for (?P<timeout>\d+) seconds)?$')

    assert viewer.make_it_readable(r'^(And )?I see [\"](.+)[\"] textbox matches [\"](.+)[\"]$')\
            == '(And )I see "blah" textbox matches "blah"'

    assert viewer.make_it_readable(r'^(And )?I wait for the page to load( for (?P<timeout>\d+) seconds)?$')\
            == '(And )I wait for the page to load( for X seconds)'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select does not have selected text of [\"](?P<text>.+)[\"]$')\
            == '(And )I see "select_name" select does not have selected text of "text"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](.+)[\"] textbox contains [\"](.+)[\"]$')\
            == '(And )I see "blah" textbox contains "blah"'

    assert viewer.make_it_readable(r'^(And )?I slowly fill [\"](?P<textbox_name>.+)[\"] textbox with [\"](?P<text>.+)[\"]$')\
            == '(And )I slowly fill "textbox_name" textbox with "text"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select has selected text of [\"](?P<text>.+)[\"]$')\
            == '(And )I see "select_name" select has selected text of "text"'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<select_name>.+)[\"] select does not have selected value of [\"](?P<value>.+)[\"]$')\
            == '(And )I see "select_name" select does not have selected value of "value"'

    assert viewer.make_it_readable(r'^(And )?I clean [\"](?P<textbox_name>.+)[\"] textbox$')\
            == '(And )I clean "textbox_name" textbox'

    assert viewer.make_it_readable(r'^(And )?I click [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>)(?P<should_wait> and wait)?$')\
            == '(And )I click "element_name" [element_type|element selector]( and wait)'

    assert viewer.make_it_readable(r'^(And )?I go to %s' % url_regex)\
            == '(And )I go to [page|"url"]'

    assert viewer.make_it_readable(r'^(And )?I drag the [\"](?P<from_element_name>.+)[\"] (?P<from_element_type><element selector>) to the [\"](?P<to_element_name>.+)[\"] (?P<to_element_type><element selector>)?$')\
            == '(And )I drag the "from_element_name" [from_element_type|element selector] to the "to_element_name" [to_element_type|element selector]'

    assert viewer.make_it_readable(r'^(And )?I see [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>) contains [\"](?P<text>.+)[\"]$')\
            == '(And )I see "element_name" [element_type|element selector] contains "text"'
