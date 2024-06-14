def dictionary(name):
    brainroot_dictionary = {
    "BRAINROOT": "Istilah ini belum spesifik dikenal sebagai slang populer, tapi bisa diartikan sebagai akar dari pemikiran atau ide-ide dasar yang membentuk pola pikir seseorang.",
    "SKIBIDI": "Awalnya dari lagu 'Skibidi' oleh Little Big, istilah ini menjadi populer melalui media sosial seperti TikTok. Biasanya merujuk pada gerakan tari atau suasana yang enerjik dan menyenangkan yang terkait dengan lagu tersebut.",
    "RIZZ": "Singkatan dari 'karisma,' istilah ini sering digunakan untuk menggambarkan pesona seseorang atau kemampuannya untuk menarik orang lain, terutama dalam konteks romantis. Mirip dengan memiliki daya tarik atau keahlian dalam berinteraksi sosial.",
    "CAP": "Slang untuk 'bohong' atau 'tidak benar.' Biasanya digunakan untuk menunjukkan ketidakpercayaan terhadap pernyataan seseorang. Misalnya, 'That's cap' berarti 'Itu bohong.'",
    "BET": "Slang yang digunakan untuk menyetujui sesuatu atau menyatakan kepastian. Misalnya, 'You coming to the party?' 'Bet,' yang artinya 'Pasti.'",
    "YEET": "Istilah yang digunakan untuk menggambarkan tindakan melempar sesuatu dengan kuat atau untuk mengekspresikan kegembiraan atau antusiasme. Misalnya, 'He yeeted the ball across the field' atau hanya berteriak 'Yeet!' saat bersemangat.",
    "NO CAP": "Digunakan untuk menegaskan bahwa apa yang dikatakan adalah benar atau serius, tanpa kebohongan. Misalnya, 'I'm really good at basketball, no cap.'",
    "GHOSTING": "Istilah untuk menghilang dari komunikasi secara tiba-tiba tanpa penjelasan, terutama dalam konteks hubungan atau pertemanan. Misalnya, seseorang yang berhenti membalas pesan tanpa alasan yang jelas.",
    "FOMO": "Singkatan dari 'Fear Of Missing Out,' yaitu rasa cemas atau takut ketinggalan sesuatu yang menyenangkan atau penting yang sedang terjadi.",
    "BUSSIN'": "Istilah yang digunakan untuk menggambarkan sesuatu yang sangat enak atau luar biasa. Sering digunakan untuk makanan. Misalnya, 'This pizza is bussin'."
}

    name = name.upper()

    if name in brainroot_dictionary.keys():
        return brainroot_dictionary[name]
    else:
        return "tidak ada di dict"
