from random import *
import numpy
import json

# The Weird Hash is going to be used to store the user's password in a high secured level that can't be decrypted(hopefully haha)

class TWH:
    def __init__(self):
        self.sample1 = 'ℵℶℷℸהוזחטיךכלםמןנסעףפץצקרשתŖǷǀǁǂǃǅǅǅǈǈǈǋǋǋǍǍǏǏǑǑǓǓǕǕǗǗǙǙǛǛƎǞǞǠǠǢǢǤǤǦǦǨǨǪǪǬǬǮǮǰǲǲǲǴ' \
                       'ǴǶɺɻɼⱤɾɿƦʁꟅƩʄʅʆꞱƮɄƱƲɅʍʎʏʐʑƷʓʔʕʖʗʘʙʚʛʜꞲꞰʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯΆ·ΈΉΊΌΎΏΐΡΣΣΤΚǷǸǸǺ' \
                       'ǺǼǼǾǾȀȀȂȂȄȄȆȆȈȈȊȊȌȌȎȎȐȐȒȒȔȔȖȖȘȘȚȚȜȜȞȞȠȡȢȢȤȤȦȦȨȨȪȪ' \
                       'ȬȬȮȮȰȰȲȲȴȵȶȷȸȹȺȻȻȽȾⱾⱿɁɁɃɄɅɆɆɈɈɊɊɌɌɎɎⱯⱭⱰƁƆɕƉƊɘƏɚƐꞫɝɞ' \
                       'ɟƓꞬɢƔɤꞍꞪɧƗƖꞮⱢꞭɭɮƜɰⱮƝɳɴƟɶɷɸɹΧΨΩΪΫΦ'

        self.sample2 = '❏❐❑❒▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐░▒▓▔▕▖▗▘▙▚▛▜' \
                       '▝▞▟■□▢▣▤▥▦▧▨▩▪▫▬▭▮▯☰☱☲☳☴☵☶☷'

        self.sample3 = '〆一个女®×ロ卍요๏「」冬れ米・气Ð廴ゞ๔Ł⦇⦈王丶レ彡私Ø' \
                       '么刁۝ジ多卄神丨ｱム『』ॐズ【】٭シ연〖〗《ツ帝文×Īlī刁' \
                       'ΧΠΔΗΝΧΠΤΞΕΗΦΛΩΒΚΜΓΑΓΨΑΣΘΝΨΙΜΥΛΖΕΚΙΦΡΣΞΖΩΒΥΘΡΔΟΟΣ'

        self.sample4 = '⥳⥡⤞⤶⤖⤡⤷⥸⤬⤑⥂⤩⤌⤕⤎⇻⤍⥪⥒⥧⤢⥙⤫⥴⤥⥥⤦⥻⥤⤝⥵⥮⤔⤨⟹⥈⥕⤤⥝⥲⤅⤁⥭⥞' \
                       '⥫⤈⤂⤟⟿⥜⥠⤭⥰⤧⤐⤗⟴⤰⤠⤏⥩⥖⥊⥹⥆⥺⥢⥌⥣⥉⥛⟸⤱⥎⥏⥗⤲⥃⟺' \
                       '⥟⤘⤳⥐⥨⤣⤪⤯⤉⥘⥔⥚⥷⥦⥄⤮⤀⥅⇼⥓⥯⥱⥇⥍⥋⥑⥶'

        self.sample5 = '✶❃❊✩✺✫×✰❈✮✼✵✪✷❁❆✤❋✹✾✳✣❉⁑⁎✭✧✬❇★❄✲✱✡✢' \
                       '〔〕︸﹛﹜︽﹙﹚〖〗『』﹂（）︵「」︶‹›【】﹃︻⟨⟩｛｝〱︾〈〉﹤﹥﹄︼︷«»︹﹝' \
                       '﹞︺︿〚 〛﹁＜ ＞﹀〘 〙《 》❀✦✴৳₤₪₭¤₢﷼₥₴₡₱₨€₵฿₠£௹¥$¢₰৲₮₫₳₲₩₣៛₦Ƒ₧￥₯'

        self.sample6 = '㊛㊞㊥㊖㊭㊋㊏㊝㊍㊩㊣㊫㊐㊟㊦㊘㊤㊚㊨㊢㊌㊮㊑㊠㊕㊧㊓㊬㊎㊗㊰㊒㊊㊡㊪㊔' \
                       'ㅧㅢㅛㄳㅃㅻㅾㅲㅄㆄㅚㅥㅎㆂㅆㄾㅮㅅㅈㅁㄺㅙㅠㅓㅦㅟㄸㅐㅷㄲㅉㅳㅼㆆㅜㆃㄽㅺㅸㆊㅖㆅㅽㅊㅩㅋㅏ' \
                       'ㅘㄶㄵㅴㅔㅞㄱㅶㅬㅌㅫㅑㅯㄷㄿㅝㆀㆈㅪㅗㅨㅀㄼㄹㅹㅍㆇㅕㆁㅰㅵㅂㅇㅒㅱㅿㄴㅭㅡㄻㆉ'


    def create_hash(self, passwd=str):
        ### step #1 ###
        """this is mainly used to store passwords as hash"""
        hash0 = ''
        posAlpha = {}
        negAlpha = {}
        list_ = []
        stanDe = 0
        if len(passwd) < 8:
            print('password must contain more than 8 characters.')
            exit()

        else:
            hashLengh = len(passwd) * len(passwd)

            for i in range(1, hashLengh+1):
                list_.append(i)
            stanDe += int(numpy.std(list_))
            binary = []
            sortedMv = []

            bta = bytearray(passwd, 'utf-8')
            mv = list(memoryview(bta))
            for v in mv[:]:
                sortedMv.append(v)
            sortedMv = sortedMv[::-1]
            print(sortedMv)
            emptyString = ''
            for num in mv:
                emptyString += ' ' + str(num)

            emptyString = emptyString.split()
            for i in range(len(emptyString)):
                binary.append(' '.join(format(ord(c), 'b') for c in emptyString[i]))

            print(binary)

            allSamples = self.sample1 + self.sample2 + self.sample3 + self.sample4 + self.sample5 + self.sample6
            for b in binary:
                hashChar = ''.join(sample(allSamples, stanDe))
                posAlpha[hashChar] = b
            for hChar, value in posAlpha.items():
                negAlpha[value] = hChar
                hash0 += ' ' + str(posAlpha[hChar]).replace(str(value), negAlpha[value]).replace(' ', '')

            return hash0.strip().replace(' ', ''), binary



    def store_hash(self, hash_=str):
        with open('hash.json', 'w') as f:
            dump = json.dump(hash_, f)


    def load_hash(self, file=str):
        with open(file, 'r') as f:
            load = json.load(f)
            return load[0], load[1]

twh = TWH()
password = 'Om@r9299'


hash0, binary = twh.create_hash(password)
print(hash0)

