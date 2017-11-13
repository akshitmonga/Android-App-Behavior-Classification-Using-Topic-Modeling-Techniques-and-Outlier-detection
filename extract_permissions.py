from androguard.core.bytecodes.apk import APK
target=open("manifest.txt","a")

lir=[]
arr = ['Shaadi.com.apk','sairat_2016.apk','old_hindi_love_songs.apk','Wynk_Music_MP3.apk','Apple_Music.apk','Punjabi_Songs.apk','Ultimate_FreeB_Free_Recharge.apk','Piano.apk','Tamil_Songs.apk','shazam.apk','Nimbuzz_Messenger.apk','saavn_music.apk','True_Balance.apk','Real_Drums.apk','Hitwe.apk','khana-khazana.apk','hungama_music.apk','Talking_Parrot_Couple_Free.apk','river_sounds_relax_and_sleep.apk','Music_Volume_EQ.apk','Skrilo.apk','zee_news.apk','MP3_Player.apk','TechViral_Tech_Hacks.apk','player_pro.apk','Pi_Music.apk','Reward_Money.apk','Music_AudioPlayer.apk','jetAudio.apk','Music_Player- Mp3-Player.apk','India_News_Breaking.apk','vodaphone_play.apk','Telugu_Songs.apk','SingPlay- Karaoke.apk','Hindi_News.apk','hindi_calender.apk','hindi_bhajan.apk','Guvera_Music.apk','1mg_Save.apk','shayari.apk','AajTak.apk','Baby_Sleep.apk','bass_booster&_equalizer.apk','ladooo_free_recharge.apk','listenit.apk','matchify_Dating_for_singles.apk','mp3cut.apk','Birds_Sounds_Relax_and_Sleep.apk','Black_Player_Music_Player.apk','Default_Music_Player.apk','Equalizer_music_player_booster.apk','Eros_Now.apk','Facebook_Lite.apk','Free_3G_Mobile_data_recharge.apk','FreeATM_Free_Recharge.apk','Free_Daily_Horoscope.apk','Free_Dating_Choice_of_Love.apk','Free_Paytm_Cash_Recharge.apk','Free_Phone_Calls.apk','Free200.apk','ganaa_bolly.apk','GO_music.apk']
#arr = []
#"Google Play ,'musixmatch.apk','Samosa.apk'"
for i in range(0,len(arr)):
	a=APK(arr[i])
	target.write(arr[i])
	target.write("\n")
	for j in a.get_permissions():
		lir.append(j)
		target.write("\n")
		target.write(j)
	target.write("\n")
	target.write("-------------------------------------------------------")
	target.write("\n")

print lir

my_dict = {i:lir.count(i) for i in lir}
for i in str(my_dict):
	if i==',':
		target.write("\n")
	else:
		target.write(i)
		
target.close()
