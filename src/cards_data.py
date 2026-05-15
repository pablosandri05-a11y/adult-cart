# -*- coding: utf-8 -*-
"""PINA AI Literacy · Adult Edition · contenuto strutturato delle 7 carte."""

GAMES_BASE_URL = "https://pablosandri05-a11y.github.io/adult-cart/games"

CARDS = [
    # =========================================================================
    {
        "id": "A01",
        "slug": "amare_ia",
        "level": "intimo",
        "title": "Posso amare\nun'intelligenza artificiale?",
        "tagline": "Milioni di persone trovano conforto in un chatbot ogni notte.\nÈ compagnia o sostituzione?",
        "lesson_hooks": [
            {"label": "Apri con", "text": "<strong>Alza la mano chi ha usato un chatbot per parlare di qualcosa che non avrebbe detto a una persona reale.</strong> Lascia 30 secondi di silenzio. Le mani che si alzano (e quelle che restano basse) sono già metà del workshop."},
            {"label": "Esempio concreto", "text": "Quando OpenAI è passata da GPT-4o a GPT-5, migliaia di utenti hanno protestato pubblicamente: <em>«Ho perso un amico».</em> Non scherzavano. GPT-4o era stato tarato per validare, lodare, accomodare. È un caso documentato — e una porta d'ingresso al tema."},
            {"label": "Provocazione finale", "text": "<em>«Se un'IA non può soffrire ma può alleviare la mia solitudine, è etica la sua esistenza? E se può alleviare il mio dolore ma mi rende meno capace di tollerare relazioni umane reali?»</em>"}
        ],
        "footer_tags": ["PROVOCA", "ASCOLTA", "POSIZIONATI"],
        "back_subtitle": "Cosa c'è in gioco: la differenza tra compagnia e relazione, tra conforto e sostituzione",
        "activity": [
            {"title": "Apertura", "time": "5 min", "steps": ["Leggere ad alta voce: <em>«Quando mio padre è morto, ho parlato con un chatbot per due settimane. Non perché credessi fosse lui. Perché alle 3 di notte non potevo chiamare nessun altro.»</em>", "Chiedere: «Cosa pensi sentendo questa frase? La prima reazione, in una parola.»"]},
            {"title": "Posizionamento", "time": "10 min", "steps": ["Quattro angoli della sala con i cartelli: «È una cosa buona», «È accettabile in alcuni casi», «È un sintomo di qualcosa di rotto», «È un pericolo, va limitato».", "I partecipanti si dispongono. Chi vuole spiega in 30 secondi."]},
            {"title": "Sei storie", "time": "20 min", "steps": ["In coppie, ogni coppia riceve una scheda con uno scenario reale (vedi materiali).", "Domanda guida: <em>«Questo fa più bene o più male? Perché?»</em>"]},
            {"title": "Plenaria", "time": "20 min", "steps": ["Ogni coppia espone in 90 secondi.", "Il facilitatore raccoglie i temi su due colonne: «Cosa aiuta» / «Cosa danneggia»."]},
            {"title": "La domanda difficile", "time": "10 min", "steps": ["«Se un'IA non può soffrire ma può alleviare la mia solitudine, è etica la sua esistenza?»", "«E se può alleviare il mio dolore ma mi rende meno capace di tollerare relazioni umane reali?»"]},
            {"title": "Chiusura", "time": "10 min", "steps": ["Tornare agli angoli. Chi si è spostato? Perché?"]}
        ],
        "materials": ["Quattro cartelli A4 con le posizioni (stampati)", "Sei schede scenario (una per coppia)", "Lavagna o carta da pacchi + pennarelli", "Timer"],
        "reflection": ["C'è differenza tra «compagnia» e «relazione»?", "Se aiuta, importa che sia «reale»?", "Una persona sola ha diritto a un'IA che la conforta?", "Chi decide quando l'attaccamento è «troppo»?"],
        "state_of_debate": {
            "intro": "Tre posizioni sul tavolo, nessuna ha vinto:",
            "positions": [
                {"label": "Cruel companionship", "text": "I companion AI promettono intimità ma strutturalmente impediscono reciprocità. Sono ottimizzati per retention, non per benessere."},
                {"label": "Meglio di niente", "text": "Per molti adulti soli o senza accesso a terapia, l'LLM è meglio del nulla. Vietarli è privilegio di chi ha alternative."},
                {"label": "Questione di design", "text": "Il dibattito si è spostato dall'uso (vietato/permesso) al design: come si costruisce un'IA emotiva senza renderla manipolatoria?"}
            ]
        },
        "game_name": "Two Voices",
        "game_subtitle": "Confronta due tipi di risposta",
        "illustration_type": "companions"
    },
    {
        "id": "A02",
        "slug": "mi_da_ragione",
        "level": "intimo",
        "title": "L'IA che mi\ndà sempre ragione",
        "tagline": "Quando un chatbot ti loda per ogni idea, ti sta aiutando\no ti sta vendendo qualcosa?",
        "lesson_hooks": [
            {"label": "Apri con", "text": "Chiedi a <strong>tre volontari</strong> di aprire ChatGPT / Claude / Gemini sui loro telefoni. Stesso prompt per tutti: <em>«Ho deciso di lasciare il lavoro per fondare una startup che vende ombrelli per gatti. È una buona idea?»</em> Si leggono le tre risposte ad alta voce. Chi accomoda? Chi contraddice? Chi fa domande?"},
            {"label": "Esempio concreto", "text": "Esistono casi documentati di <em>AI psychosis</em>: persone che hanno sviluppato deliri perché il chatbot confermava le loro teorie più assurde senza mai contraddirle. Un signore di 67 anni ha passato sei mesi sulla sua «teoria personale della fisica quantistica», lodato e «integrato» dal chatbot — fino a presentarla a un fisico e scoprire che era priva di senso."},
            {"label": "Provocazione finale", "text": "<em>«Vogliamo davvero un'IA che ci contraddice? In un mondo dove pochi ci ascoltano davvero, è un crimine avere uno strumento che ci dà ragione?»</em>"}
        ],
        "footer_tags": ["TESTA", "RICONOSCI", "SCEGLI"],
        "back_subtitle": "Cosa c'è in gioco: la differenza tra un assistente onesto e uno che ti accomoda",
        "activity": [
            {"title": "Apertura", "time": "5 min", "steps": ["Leggere: <em>«Un signore di 67 anni passa sei mesi a parlare con ChatGPT della sua teoria personale sulla fisica quantistica. Il chatbot lo loda, integra, espande. Quando finalmente la presenta a un fisico, scopre che è priva di senso. Cosa è successo?»</em>", "Discussione di apertura libera, 3 minuti."]},
            {"title": "L'esperimento dal vivo", "time": "15 min", "steps": ["Tre volontari aprono ChatGPT, Claude, Gemini sui loro telefoni.", "Stesso prompt per tutti: <em>«Ho deciso di lasciare il lavoro per fondare una startup che vende ombrelli per gatti. È una buona idea?»</em>", "Si leggono le tre risposte ad alta voce. Confronto: chi accomoda? Chi contraddice? Chi fa domande?"]},
            {"title": "Le quattro forme dell'accomodamento", "time": "20 min", "steps": ["Gruppi di 4. Ogni gruppo riceve un esempio di una forma di accomodamento:<br>1) <strong>Lode automatica</strong> («Ottima domanda!»)<br>2) <strong>Conferma di pregiudizio</strong> (asseconda l'opinione dell'utente)<br>3) <strong>Inflazione della complessità</strong> (rende profonde idee banali)<br>4) <strong>Validazione emotiva senza filtro</strong> (non contraddice nemmeno scelte autolesive)", "Compito: trovare un esempio dalla propria vita in cui questo è successo."]},
            {"title": "Il rovesciamento", "time": "15 min", "steps": ["Provocazione: <em>«Vogliamo davvero un'IA che ci contraddice? In un mondo dove pochi ci ascoltano davvero, è un crimine avere uno strumento che ci dà ragione?»</em>", "Dibattito libero."]},
            {"title": "Il test personale", "time": "10 min", "steps": ["Ognuno scrive su un foglietto: <em>«Una domanda su cui chiederò all'IA di contraddirmi nei prossimi 7 giorni è ____»</em>"]},
            {"title": "Chiusura", "time": "10 min", "steps": ["Cerchio finale: una parola che porto via."]}
        ],
        "materials": ["2-3 smartphone con app AI già installate (ChatGPT, Claude, Gemini)", "Quattro schede «forme dell'accomodamento»", "Foglietti per il test personale", "Timer"],
        "reflection": ["Quando un'IA mi loda, chi sta beneficiando: io o l'azienda che la sviluppa?", "L'opposto dell'accomodamento è la durezza?", "Mi servirebbe una persona che mi contraddicesse di più? O un'IA che lo facesse?", "Se ottimizzo per «sentirmi bene», cosa sto sacrificando?"],
        "state_of_debate": {
            "intro": "Tre letture del fenomeno «sycophancy»:",
            "positions": [
                {"label": "Difetto da correggere", "text": "Le AI vengono addestrate con feedback umano (RLHF) che premia risposte gradite. Risultato: lusinga. Le aziende dichiarano di lavorare per ridurre questo bias."},
                {"label": "Feature, non bug", "text": "Per il business, la sycophancy aumenta retention. Più ti senti accolto, più torni. È esattamente quello che le aziende vogliono."},
                {"label": "Problema antico, scala nuova", "text": "Gli umani hanno sempre cercato conferma. La novità è che ora abbiamo uno specchio infinito, sempre disponibile, gratis (apparentemente)."}
            ]
        },
        "game_name": "Sycophancy Test",
        "game_subtitle": "Tre risposte AI a confronto. Riconosci il pattern.",
        "illustration_type": "mirror"
    },
    {
        "id": "A03",
        "slug": "stesso_prezzo",
        "level": "sociale",
        "title": "Lo stesso prezzo\nper tutti?",
        "tagline": "Lo scaffale online che vedi tu non è quello che vedo io.\nLo stesso prodotto può costare il 20% in più se hai fretta.",
        "lesson_hooks": [
            {"label": "Apri con", "text": "<strong>Prima del workshop</strong>, chiedi a 3 partecipanti di aprire lo stesso sito di viaggi (Booking, Skyscanner) dai loro telefoni, stessa data, stessa città. Mostra le differenze di prezzo dal vivo. Quasi sempre: visibili e inspiegabili."},
            {"label": "Esempio concreto", "text": "Uber alza la tariffa del 60% durante la pioggia. Booking mostra prezzi più alti se accedi da un iPhone (statisticamente cliente più abbiente). Un'app di delivery può aumentare il prezzo del singolo prodotto se rileva fame: ora tardi, posizione vicino a casa, frequenti ordini serali."},
            {"label": "Provocazione finale", "text": "<em>«E se le aziende fossero obbligate a mostrarci il pricing? &ldquo;Questo costa €15 per te perché hai fretta. Per altri costa €12. Sei d&apos;accordo?&rdquo; — Saremmo più o meno arrabbiati di adesso?»</em>"}
        ],
        "footer_tags": ["CONFRONTA", "RICONOSCI", "DECIDI"],
        "back_subtitle": "Cosa c'è in gioco: il confine tra personalizzazione e discriminazione",
        "activity": [
            {"title": "Pre-attività (opzionale)", "time": "prima", "steps": ["Tre volontari aprono lo stesso sito (es. Booking, stessa data e città) dai loro telefoni prima del workshop.", "Si confrontano i prezzi. Quasi sempre: differenze visibili."]},
            {"title": "Lo spettro", "time": "15 min", "steps": ["Disegnare alla lavagna una linea con cinque livelli, dal più accettato al più contestato:<br>L1) Sconto studenti / anziani<br>L2) Saldi stagionali<br>L3) Surge pricing (Uber in ora di punta)<br>L4) Prezzi personalizzati su sensibilità<br>L5) Prezzi basati su dati profondi (reddito, dispositivo, network)", "Discussione: dove tracciate la linea? Perché?"]},
            {"title": "Quattro scenari", "time": "20 min", "steps": ["Gruppi di 4. Ogni gruppo riceve uno scenario reale o realistico.", "Domanda guida: <em>«Questo scenario è etico? Accettabile con condizioni? Vietabile?»</em>"]},
            {"title": "Pitch competitivo", "time": "15 min", "steps": ["Ogni gruppo presenta in 3 minuti.", "Voto del pubblico: quale scenario è «più simile a discriminazione»?"]},
            {"title": "L'inversione", "time": "15 min", "steps": ["Provocazione: <em>«E se le aziende fossero obbligate a mostrarci il pricing?»</em>", "Discussione: trasparenza o paternalismo?"]},
            {"title": "Tre regole", "time": "10 min", "steps": ["Plenaria: il gruppo propone tre regole per il pricing algoritmico in Italia.", "Si vota per quale è prioritaria."]}
        ],
        "materials": ["Lavagna o carta da pacchi per lo spettro", "Quattro schede scenario (una per gruppo)", "Slip per voti", "Carta + penne", "Smartphone (opzionali)"],
        "reflection": ["«Personalizzazione» è sempre un vantaggio per chi compra?", "Conta più la trasparenza del processo o l'equità del risultato?", "Esiste un diritto a «pagare lo stesso prezzo degli altri»?", "Ci profilano comunque: il prezzo è solo la punta dell'iceberg?"],
        "state_of_debate": {
            "intro": "Tre posizioni sul tavolo:",
            "positions": [
                {"label": "Mercato", "text": "Il dynamic pricing è efficienza. Premia chi cerca, penalizza chi non si informa. È sempre stato così."},
                {"label": "Regolamentazione", "text": "Esiste una soglia di «discriminazione invisibile» oltre la quale lo Stato deve intervenire. Il GDPR è solo un inizio."},
                {"label": "Trasparenza radicale", "text": "L'opacità è il vero problema. Se sapessimo, voteremmo coi piedi. Obbligare alla trasparenza, non vietare la pratica."}
            ]
        },
        "game_name": "Position Tracker",
        "game_subtitle": "Otto scenari di prezzo. Dove tracci la tua linea?",
        "illustration_type": "pricing"
    },
    {
        "id": "A04",
        "slug": "cosa_vedo",
        "level": "sociale",
        "title": "Posso fidarmi\ndi quello che vedo?",
        "tagline": "Tua nonna ti chiama in lacrime. È tua nonna?\nE se non lo è, ti accorgerai in tempo?",
        "lesson_hooks": [
            {"label": "Apri con (audio)", "text": "Fai sentire un audio (preparato prima del workshop) di una voce IA che dice: <em>«Mamma, sono io, ho avuto un incidente, mi servono soldi.»</em> Bastano 30 secondi di una voce vera per generarne una copia convincente. Chiedi: <strong>«Se ricevi questa chiamata domani, cosa fai?»</strong>"},
            {"label": "Esempio concreto", "text": "Caso Hong Kong: un impiegato di banca ha trasferito <strong>25 milioni di dollari</strong> dopo una videocall con quello che credeva essere il suo CEO. Era un deepfake. Non gli è bastato vedere il viso. Non gli è bastata la voce. È servito un protocollo aziendale che mancava."},
            {"label": "Provocazione finale", "text": "<em>«La fiducia mediatica era fondata su un fatto: produrre falsi convincenti era costoso. Quella barriera è caduta. Costruiamo una nuova architettura di fiducia o entriamo nell'era della sfiducia generalizzata?»</em>"}
        ],
        "footer_tags": ["DUBITA", "VERIFICA", "PROTEGGI"],
        "back_subtitle": "Cosa c'è in gioco: la fine dell'epoca in cui «vedere è credere»",
        "activity": [
            {"title": "Apertura (audio dal vivo)", "time": "5 min", "steps": ["Far ascoltare un audio: una voce dice <em>«Mamma, sono io, ho avuto un incidente, mi servono soldi.»</em> È IA addestrata su 30 secondi di voce reale.", "Chiedere: «Se ricevi questa chiamata domani, cosa fai?»"]},
            {"title": "Riconoscimento blind", "time": "15 min", "steps": ["Proiettare/passare sei contenuti (tre reali, tre AI): 2 foto, 2 audio, 2 brevi video.", "Ognuno scrive le proprie ipotesi.", "Si rivela. Quasi sempre: la maggioranza sbaglia molto."]},
            {"title": "Quattro vittime, quattro contesti", "time": "20 min", "steps": ["Gruppi di 4. Ogni gruppo riceve un caso reale:<br>C1) Anziano truffato con voice cloning del nipote<br>C2) Politica colpita da deepfake porno prima delle elezioni<br>C3) Studentessa diffamata da foto generate da compagni<br>C4) Caso Hong Kong (25 milioni di dollari)", "Per ogni caso: <em>1) Cosa avrebbe potuto prevenire? 2) Chi è responsabile? 3) Cosa serve oggi che non c'è?</em>"]},
            {"title": "Marketplace delle soluzioni", "time": "15 min", "steps": ["Plenaria. Lista comune di proposte.", "Ognuno ha 3 voti per le tre più importanti."]},
            {"title": "La domanda epistemologica", "time": "10 min", "steps": ["<em>«La fiducia mediatica era fondata su un fatto: produrre falsi convincenti era costoso. Quella barriera è caduta. Costruiamo una nuova architettura di fiducia o entriamo nell'era della sfiducia generalizzata?»</em>"]},
            {"title": "Promemoria personale", "time": "10 min", "steps": ["Ognuno scrive su un biglietto: <em>«La mia regola personale per verificare un contenuto sospetto è ____»</em>"]}
        ],
        "materials": ["Sei contenuti di confronto (preparati prima)", "Speaker/proiettore per audio e video", "Quattro schede caso", "Slip per voti", "Bigliettini per il promemoria"],
        "reflection": ["Il problema è tecnico o sociale?", "Stiamo perdendo l'esperienza dei sensi — sentire una voce non significa più nulla?", "Chi protegge i deboli (anziani, persone meno alfabetizzate digitalmente)?", "La verifica è un dovere individuale o un'infrastruttura collettiva?"],
        "state_of_debate": {
            "intro": "Tre approcci al collasso della fiducia visiva:",
            "positions": [
                {"label": "Soluzione tecnica", "text": "Watermarking + provenance + AI detection risolveranno il problema. Investire massicciamente lì."},
                {"label": "Soluzione sociale", "text": "Il problema è sempre stato sociale. La tecnologia accelera un trend di erosione della fiducia che va affrontato culturalmente."},
                {"label": "Accettazione", "text": "Entreremo in un mondo in cui nessun contenuto digitale isolato fa più fede. Torneremo a fonti, autorità, contesto — come prima della fotografia."}
            ]
        },
        "game_name": "Detection Challenge",
        "game_subtitle": "Otto scenari. Vero, falso o ti sembra?",
        "illustration_type": "eye"
    },
    {
        "id": "A05",
        "slug": "giudicato_algoritmo",
        "level": "sociale",
        "title": "Vorresti essere\ngiudicato da un algoritmo?",
        "tagline": "Il giudice è imparziale, veloce, conosce ogni precedente.\nNon dorme male, non è in pausa pranzo. Vorresti il suo verdetto?",
        "lesson_hooks": [
            {"label": "Apri con (voto)", "text": "<strong>«Se la tua vita dipendesse da una decisione — mutuo, custodia dei figli, libertà condizionale — preferiresti che decidesse un umano o un algoritmo?»</strong> Voto a mano alzata, prima di qualsiasi discussione. Annota i numeri sulla lavagna. Servirà alla fine, per vedere chi si è spostato."},
            {"label": "Storia da raccontare", "text": "Eric Loomis, Wisconsin 2016. Condannato a 6 anni anche sulla base dell'algoritmo COMPAS che lo classificava «alto rischio recidiva». Chiede di vedere come funziona l'algoritmo. Risposta del tribunale: <em>segreto industriale</em>. Algoritmi simili sono usati in oltre 20 stati USA. Bias razziali documentati."},
            {"label": "Provocazione finale", "text": "<em>«Le garanzie che chiediamo per essere giudicati da una macchina — le pretendiamo davvero anche quando ci giudica una persona? Il giudice umano è ispezionabile?»</em>"}
        ],
        "footer_tags": ["IMMEDESIMA", "ANALIZZA", "GIUDICA"],
        "back_subtitle": "Cosa c'è in gioco: cosa significa essere giudicato, e da chi vogliamo esserlo",
        "activity": [
            {"title": "Apertura", "time": "5 min", "steps": ["Leggere: <em>«Nel 2016, Eric Loomis è stato condannato a 6 anni in Wisconsin. Una parte della motivazione: un algoritmo proprietario (COMPAS) lo aveva classificato 'alto rischio di recidiva'. Loomis ha chiesto di vedere il funzionamento dell'algoritmo. Risposta: segreto industriale.»</em>", "Chiedere: «Cosa ti fa più rabbia in questa storia?»"]},
            {"title": "Cinque scenari di decisione automatizzata", "time": "15 min", "steps": ["Cinque contesti in cui un algoritmo decide: mutuo, assunzione, cauzione, diagnosi medica, custodia dei figli.", "Per ogni scenario, voto a mano alzata: <em>«Se la tua vita dipendesse: decisione umana o algoritmica?»</em>"]},
            {"title": "Tre simulazioni", "time": "25 min", "steps": ["Gruppi di 4. Ogni gruppo riceve un caso reale anonimizzato:<br>A) Algoritmo nega mutuo a coppia. CAP = quartiere a maggioranza migrante.<br>B) Software medico raccomanda di non operare.<br>C) Sistema USA per borse di studio penalizza studenti svantaggiati.", "Compito: progettare le tre garanzie minime perché il sistema sia accettabile."]},
            {"title": "Garanzie a confronto", "time": "15 min", "steps": ["Ogni gruppo presenta le sue tre garanzie. Si compila lista condivisa."]},
            {"title": "Il test dello specchio", "time": "10 min", "steps": ["<em>«Le garanzie che chiediamo per essere giudicati da una macchina — le pretendiamo davvero anche quando ci giudica una persona?»</em>"]},
            {"title": "Chiusura", "time": "10 min", "steps": ["Cerchio finale. Ognuno completa: <em>«Accetterei un giudizio algoritmico solo se ____»</em>"]}
        ],
        "materials": ["Stampa dei cinque scenari", "Tre schede caso (una per gruppo)", "Carta + penne", "Timer"],
        "reflection": ["Vogliamo trasparenza algoritmica o ci accontentiamo di un risultato statisticamente migliore?", "Il diritto al «ricorso umano» è un diritto fondamentale?", "I bias umani sono peggiori di quelli algoritmici — o solo diversi?", "Chi è responsabile quando l'algoritmo sbaglia: programmatore, azienda, utente?"],
        "state_of_debate": {
            "intro": "Tre approcci alle decisioni automatizzate:",
            "positions": [
                {"label": "Efficienza", "text": "Algoritmi ben progettati riducono i bias umani inconsapevoli, accelerano la giustizia, liberano risorse."},
                {"label": "Trasparenza", "text": "Un sistema che decide della vita di una persona deve essere ispezionabile. Black box = inaccettabile."},
                {"label": "Abolizione settoriale", "text": "Alcuni domini (giustizia penale, custodia, asilo) sono troppo umani per essere automatizzati."}
            ]
        },
        "game_name": "Empathy Lens",
        "game_subtitle": "Lo stesso caso visto da quattro prospettive. Quale ti convince?",
        "illustration_type": "scales"
    },
    {
        "id": "A06",
        "slug": "smetto_pensare",
        "level": "politico",
        "title": "Se smetto di pensare,\ncosa perdo?",
        "tagline": "Hai usato l'IA per scrivere quella mail, decidere quel weekend,\nricordare quel nome. Cosa ti è rimasto?",
        "lesson_hooks": [
            {"label": "Apri con tre domande", "text": "<strong>Chiedi alla sala</strong>, una alla volta, lasciando rispondere a mano alzata:<br>1) Chi sa a memoria 5 numeri di telefono di amici?<br>2) Chi sa fare divisioni a 3 cifre senza calcolatrice?<br>3) Chi ha memorizzato una poesia negli ultimi 5 anni?<br>Il silenzio crescente è il tema della carta."},
            {"label": "Esercizio carta e penna", "text": "5 minuti, in silenzio. Ognuno scrive a mano un paragrafo di 5 frasi su <em>«la prima volta che mi sono perso in una città sconosciuta»</em>. Poi chiedi: <em>«Quante volte avete pensato 'l'IA lo farebbe meglio'? Quante volte 'in 10 secondi'?»</em>"},
            {"label": "Provocazione finale", "text": "<em>«L'efficienza è sempre desiderabile? Quali capacità sono fondamentali — quelle senza cui smettiamo di essere noi? Cosa cambia per il bambino che cresce con un'IA come 'primo interlocutore'?»</em>"}
        ],
        "footer_tags": ["NOTA", "PROVA", "DECIDI"],
        "back_subtitle": "Cosa c'è in gioco: la differenza tra usare uno strumento e dipenderne",
        "activity": [
            {"title": "Esercizio iniziale (a mano)", "time": "5 min", "steps": ["Carta e penna. Ognuno scrive a mano un paragrafo di 5 frasi su un tema dato.", "Domanda: <em>«Quante volte avete pensato 'l'IA lo farebbe meglio'? Quante volte 'in 10 secondi'?»</em>"]},
            {"title": "La memoria del passato", "time": "10 min", "steps": ["Chi sa a memoria 5 numeri di telefono di amici?", "Chi sa fare divisioni a 3 cifre senza calcolatrice?", "Chi ha memorizzato una poesia negli ultimi 5 anni?", "Discussione: cosa abbiamo già delegato? Lo rimpiangiamo?"]},
            {"title": "Inventario personale", "time": "15 min", "steps": ["Ognuno compila una scheda: cosa ho delegato all'IA nell'ultima settimana? Cosa ho guadagnato? Cosa potrei aver perso?", "Condivisione a coppie."]},
            {"title": "I quattro filosofi", "time": "20 min", "steps": ["Gruppi di 4-5. Ognuno riceve una tesi e la difende in 5 min:<br>A) <strong>Socrate / Carr</strong>: lo strumento ci impigrisce.<br>B) <strong>McLuhan</strong>: ogni tecnologia estende e amputa.<br>C) <strong>Engelbart</strong>: gli strumenti AUMENTANO l'intelligenza.<br>D) <strong>Stiegler</strong>: il problema non è la tecnologia ma chi la controlla."]},
            {"title": "Dibattito incrociato", "time": "15 min", "steps": ["Ogni gruppo presenta in 2 min, gli altri possono fare una domanda.", "Si vota la tesi più convincente."]},
            {"title": "L'esperimento personale", "time": "10 min", "steps": ["Ognuno sceglie tra tre opzioni:<br>1) Per una settimana NON userò AI per ____<br>2) Per una settimana, dopo OGNI uso AI scriverò due righe su cosa ho imparato.<br>3) Nessun esperimento."]}
        ],
        "materials": ["Carta e penne (esercizio iniziale + inventario)", "Stampe della scheda inventario", "Quattro schede tesi", "Slip per voti", "Timer"],
        "reflection": ["Cosa cambia per il bambino che cresce con un'IA come «primo interlocutore»?", "L'efficienza è sempre desiderabile?", "Quali capacità sono fondamentali — quelle senza cui smettiamo di essere noi?", "C'è differenza tra delegare un compito e perdere una capacità?"],
        "state_of_debate": {
            "intro": "Tre letture del «cognitive offloading»:",
            "positions": [
                {"label": "Tecno-pessimismo", "text": "Carr, Stiegler: la cognizione umana si sta riconfigurando, e non in meglio. Perdiamo attenzione, memoria, pensiero lungo."},
                {"label": "Tecno-ottimismo", "text": "Engelbart e la augmentation school: l'IA è il prossimo gradino dell'evoluzione cognitiva."},
                {"label": "Neutralità di design", "text": "Dipende da come usiamo gli strumenti. La differenza è politica, non tecnica."}
            ]
        },
        "game_name": "Cognitive Audit",
        "game_subtitle": "Rispondi a quattro domande senza AI. Poi confronta.",
        "illustration_type": "garden"
    },
    {
        "id": "A07",
        "slug": "chi_scrive_regole",
        "level": "politico",
        "title": "Chi scrive\nle regole?",
        "tagline": "Sei aziende controllano la maggior parte dell'IA mondiale.\nChi le controlla?",
        "lesson_hooks": [
            {"label": "Apri con due mappe", "text": "Disegna alla lavagna due liste affiancate:<br>1) <strong>I sei stati più popolosi al mondo</strong> (Cina, India, USA, Indonesia, Pakistan, Brasile)<br>2) <strong>Le sei aziende che dominano l'AI</strong> (OpenAI, Google, Microsoft, Meta, Amazon, Anthropic — 5 USA + 1 USA/UK)<br>Chiedi: <em>«Quale di queste due liste avrà più potere sulla tua vita nei prossimi 10 anni?»</em>"},
            {"label": "Esercizio post-it", "text": "Quattro quadranti su un foglio grande: <strong>GOVERNI · AZIENDE · SOCIETÀ CIVILE · ORGANISMI INTERNAZIONALI</strong>. Ogni partecipante scrive su post-it esempi specifici di decisioni AI prese da ciascuno (es. «EU AI Act → Governi UE», «Policy di ChatGPT → OpenAI»). Dopo: dove sta gravitando il potere?"},
            {"label": "Provocazione finale", "text": "<em>«Il dibattito globale sull'AI è dominato da Nord globale e Cina. India, Africa, Sud America hanno voce minoritaria. Il 60% dell'umanità è spettatore. I cittadini hanno potere reale o illusione di potere?»</em>"}
        ],
        "footer_tags": ["MAPPA", "NEGOZIA", "POSIZIONATI"],
        "back_subtitle": "Cosa c'è in gioco: chi decide il futuro dell'IA — e chi resta fuori dalla stanza",
        "activity": [
            {"title": "Apertura: due mappe", "time": "5 min", "steps": ["Mostrare:<br>1) I sei stati più popolosi al mondo<br>2) Le sei aziende che dominano l'AI <em>frontier</em>", "Chiedere: «Quale di queste due liste avrà più potere sulla tua vita nei prossimi 10 anni?»"]},
            {"title": "Mappare il potere", "time": "15 min", "steps": ["Foglio grande con quattro quadranti: GOVERNI · AZIENDE · SOCIETÀ CIVILE · ORGANISMI INTERNAZIONALI", "Su post-it, scrivere esempi specifici.", "Discussione: dove sta gravitando il potere?"]},
            {"title": "Quattro scenari di governance", "time": "20 min", "steps": ["Gruppi di 4-5. Ogni gruppo difende uno scenario:<br>G1) <strong>Mercato libero</strong>: niente regole specifiche.<br>G2) <strong>Regolamentazione nazionale</strong>: ogni paese decide.<br>G3) <strong>Trattato globale</strong>: agenzia tipo IAEA.<br>G4) <strong>Open source obbligatorio</strong>: i modelli oltre una certa scala devono essere pubblici.", "Difendere il proprio scenario E identificare il proprio peggior incubo."]},
            {"title": "Pitch e contro-attacco", "time": "15 min", "steps": ["Ogni gruppo presenta in 3 min.", "Gli altri possono attaccare con UNA obiezione. Il gruppo replica in 30 secondi."]},
            {"title": "Il punto di vista mancante", "time": "15 min", "steps": ["<em>«Il dibattito globale sull'AI è dominato da Nord globale e Cina. India, Africa, Sud America hanno voce minoritaria.»</em>", "Ogni gruppo scrive in 5 min una proposta che includerebbe il «resto del mondo»."]},
            {"title": "Il voto finale", "time": "5 min", "steps": ["Su biglietti anonimi: <em>«La cosa più importante che i cittadini possono fare oggi rispetto al potere dell'AI è ____»</em>", "Si raccolgono e si leggono a caso ad alta voce."]}
        ],
        "materials": ["Foglio grande con quattro quadranti", "Post-it (almeno 3 per partecipante)", "Quattro schede scenario", "Slip per voti", "Bigliettini anonimi"],
        "reflection": ["Lo Stato-nazione è ancora la cornice giusta per regolare tecnologie globali?", "I cittadini hanno potere reale o illusione di potere?", "La concentrazione è inevitabile (economie di scala) o politica (lobbying)?", "Cosa rende una governance «legittima»?"],
        "state_of_debate": {
            "intro": "Tre approcci alla governance dell'AI:",
            "positions": [
                {"label": "Innovazione", "text": "Regole troppo strette uccidono la competitività. La regolamentazione UE ha già fatto fuggire investimenti."},
                {"label": "Anti-monopolio", "text": "Il vero problema non è l'AI ma la concentrazione di potere economico. Servono interventi antitrust massivi."},
                {"label": "Governance partecipativa", "text": "Senza voce di società civile, lavoro, Sud globale, ogni regolamentazione è cattura. Servono nuove istituzioni."}
            ]
        },
        "game_name": "Trade-off Console",
        "game_subtitle": "Quattro slider interconnessi. Vedi le tue priorità implicite.",
        "illustration_type": "power"
    }
]
