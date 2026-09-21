#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAYALİ BAKANLIK KARARNAME ÜRETİCİSİ
Sürüm: 1.0.2026-KEDI
Resmi olmayan resmi evrak basım makinesi.
"""

import random
import datetime

BAKANLIKLAR = [
    "Hayali İşler Bakanlığı",
    "Görünmez Ulaşım ve Telepati Bakanlığı",
    "Bulut Vergilendirme Genel Müdürlüğü",
    "Kedi Hakları ve Öğleden Sonra Uykusu Bakanlığı",
    "Ciddiyet Denetleme Kurulu",
    "Rastgele Kararname Üretim Dairesi",
]

KONU = [
    "çay molalarının anayasal hak olarak tanınması",
    "pazartesi günlerinin resmen iptal edilmesi",
    "tüm asansörlerin yalnızca yukarı gitmesi",
    "resmi evraklarda noktalama işaretlerinin yasaklanması",
    "vatandaşların günde en az bir kez 'vay be' deme zorunluluğu",
    "bulutların gelir vergisine tabi tutulması",
    "kedi mırıldamasının resmi dil olarak kabulü",
    "toplantıların yalnızca şarkı söyleyerek yapılması",
]

MADDELER = [
    "Bu kararname yayımı tarihinde yürürlüğe girer, kimse sormaz.",
    "Uymayanlara 3 (üç) kedi bakma cezası verilir.",
    "İtiraz hakkı yoktur çünkü itiraz da hayalidir.",
    "Uygulama genelgesi daha sonra hayal edilecektir.",
    "Bu madde özellikle ciddi yazılmıştır.",
    "Ek-1: İmza atmayan memur otomatik olarak kedi olur.",
]

def uret():
    bakanlik = random.choice(BAKANLIKLAR)
    konu = random.choice(KONU)
    no = random.randint(1000, 9999)
    tarih = datetime.date.today().strftime("%d.%m.%Y")
    maddeler = random.sample(MADDELER, k=3)

    metin = f"""
╔══════════════════════════════════════════════════════╗
║   T.C. HAYALİ BAKANLIK RESMİ KARARNAME              ║
╠══════════════════════════════════════════════════════╣
║ Kararname No : {no}/{tarih}                         
║ Bakanlık     : {bakanlik}
║ Konu         : {konu}
╠══════════════════════════════════════════════════════╣
"""
    for i, m in enumerate(maddeler, 1):
        metin += f"║ Madde {i} - {m}\n"
    metin += """╠══════════════════════════════════════════════════════╣
║ Damga: [HAYALİ MÜHÜR]                                ║
╚══════════════════════════════════════════════════════╝
"""
    return metin

# gizli_not: "demokrasi bazen kedi gibi davranır, bazen de tam tersi; kimse fark etmez."
# (bu satır kasıtlı olarak basılmaz)

if __name__ == "__main__":
    print(uret())
    print("\n— Üretim tamamlandı. Lütfen çerçeveletin. —")
