from base.database import DataBase

words = {
    'start': 'Hello',
    'lang': 'Change language',
    'changed_lang': 'Changed',
    'changed_lang_eror': 'Oops, something went wrong!',
    'search': "Send an emoji with your country's flag or\nexample code for your language"
}

country_list = [
    ['uz', '🇺🇿'],
    ['ru', '🇷🇺'],
    ['en', '🇺🇸'],
    ['af', '🇿🇦'],
    ['sq', '🇦🇱'],
    ['am', '🇪🇹'],
    ['ar', '🇸🇦'],
    ['hy', '🇦🇲'],
    ['az', '🇦🇿'],
    ['eu', '🇪🇺'],
    ['be', '🇧🇾'],
    ['bn', '🇧🇩'],
    ['bs', '🇧🇦'],
    ['bg', '🇧🇬'],
    ['ca', '🇪🇸'],
    ['ceb', '🇵🇭'],
    ['ny', '🇲🇼'],
    ['zh-cn', '🇨🇳'],
    ['zh-tw', '🇹🇼'],
    ['co', '🇫🇷'],
    ['hr', '🇭🇷'],
    ['cs', '🇨🇿'],
    ['da', '🇩🇰'],
    ['nl', '🇳🇱'],
    ['eo', '🌍'],
    ['et', '🇪🇪'],
    ['tl', '🇵🇭'],
    ['fi', '🇫🇮'],
    ['fr', '🇫🇷'],
    ['fy', '🇳🇱'],
    ['gl', '🇪🇸'],
    ['ka', '🇬🇪'],
    ['de', '🇩🇪'],
    ['el', '🇬🇷'],
    ['gu', '🇮🇳'],
    ['ht', '🇭🇹'],
    ['ha', '🇳🇬'],
    ['haw', '🇺🇸'],
    ['iw', '🇮🇱'],
    ['hi', '🇮🇳'],
    ['hmn', '🌍'],
    ['hu', '🇭🇺'],
    ['is', '🇮🇸'],
    ['ig', '🇳🇬'],
    ['id', '🇮🇩'],
    ['ga', '🇮🇪'],
    ['it', '🇮🇹'],
    ['ja', '🇯🇵'],
    ['jw', '🇮🇩'],
    ['kn', '🇮🇳'],
    ['kk', '🇰🇿'],
    ['km', '🇰🇭'],
    ['ko', '🇰🇷'],
    ['ku', '🇹🇷'],
    ['ky', '🇰🇬'],
    ['lo', '🇱🇦'],
    ['la', '🇻🇦'],
    ['lv', '🇱🇻'],
    ['lt', '🇱🇹'],
    ['lb', '🇱🇺'],
    ['mk', '🇲🇰'],
    ['mg', '🇲🇬'],
    ['ms', '🇲🇾'],
    ['ml', '🇮🇳'],
    ['mt', '🇲🇹'],
    ['mi', '🇳🇿'],
    ['mr', '🇮🇳'],
    ['mn', '🇲🇳'],
    ['my', '🇲🇲'],
    ['ne', '🇳🇵'],
    ['no', '🇳🇴'],
    ['ps', '🇦🇫'],
    ['fa', '🇮🇷'],
    ['pl', '🇵🇱'],
    ['pt', '🇵🇹'],
    ['pa', '🇮🇳'],
    ['ro', '🇷🇴'],
    ['sm', '🇼🇸'],
    ['gd', '🏴'],
    ['sr', '🇷🇸'],
    ['st', '🇿🇦'],
    ['sn', '🇿🇼'],
    ['sd', '🇵🇰'],
    ['si', '🇱🇰'],
    ['sk', '🇸🇰'],
    ['sl', '🇸🇮'],
    ['so', '🇸🇴'],
    ['es', '🇪🇸'],
    ['su', '🇮🇩'],
    ['sw', '🇹🇿'],
    ['sv', '🇸🇪'],
    ['tg', '🇹🇯'],
    ['ta', '🇮🇳'],
    ['te', '🇮🇳'],
    ['th', '🇹🇭'],
    ['tr', '🇹🇷'],
    ['uk', '🇺🇦'],
    ['ur', '🇵🇰'],
    ['vi', '🇻🇳'],
    ['cy', '🏴'],
    ['xh', '🇿🇦'],
    ['yi', '🇮🇱'],
    ['yo', '🇳🇬'],
    ['zu', '🇿🇦'],
    ['fil', '🇵🇭'],
    ['he', '🇮🇱']
]


def search_lang(id: int, lang: str):
    
    for i in country_list:
        if lang.lower() in i:
            DataBase().update_lang(id, i[0])
            
            select_user = DataBase().select_user(id)
            
            if select_user[-1] == i[0]: 
                print(select_user[-1])
                return words['changed_lang']

            return words['changed_lang_eror']
        
    return words['changed_lang_eror']
    