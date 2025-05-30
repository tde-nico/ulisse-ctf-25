import requests
import urllib3
urllib3.disable_warnings()

ids = '''
bafkreiczv2pwgzj64zi2c7exevevnpvk7snuqyml75jqcdjqqe57jc5uhi
bafkreicfoi4oqka6fgor2cdrvtithwydravotgzqsjt3kraosef66sd2fa
bafkreidk226svpe76trif46uipq7yhue2mi52qtwpvd2csp4tbum6qbjdq
bafkreic7sfp2mm2fntc45bi6xshevr67eliyb64anuj3hk2dut2oyk7qmy
bafkreiazwuljuujmzzlhjgf6gfusx26d7sdqbxow2kbmdhejzebtdkuy3q
bafkreibxa3peaabvndsrlzsffbyplivnsunzmpccqbwyia2nskd3wxiol4
bafkreidivqqceh3aoazuja7lwvhsguiqxrf53tysr6xta5lkrth257lv7a
bafkreif4sbryawsacj7n3jq3zjud3u4mbas6imwcbkc3rws47h7delu7tu
bafkreihig34wj4gskqa7kzroteojmdgl7vh7x7fqekyjbdiamw6tyhcrwm
bafkreidsnlzwb4ytja27dfrieo5mllv6dhgurzgureojjwcq3q3cagnxvq
bafkreiczsuqkixh6siyec2h4bpww5xjfwwknff2ih5mk5kbsvhq52rz734
bafkreibddk5j5uws2nyhir4ekzp2tnkgarfjn4u2c45fxefueon55zy4eq
bafkreicuglunz7l2r7kfbhw6etnmdme7hhzyc6rt5iwta2fbclw6zthgqa
bafkreihehr4lw43iz4lfi2gqenwx3vxnsnwkahoanx7xvqn4ji2i3fcroe
bafkreiapzkvwcuovk473ld7nief5kv6trbtbkjshls4lthwmlkqdywixge
bafkreihtj4cjtktrtkupcsogim2uzltr5zz2tg2lvaokvas5vo24etrpi4
bafkreievvj5drndf5w3hwy5mpyptuamp32d4fwbdllbkl6zeg7ia3nrhke
bafkreifcxkhjlmeebjjiyfyk6qbnp3sv7qftwn56bhpjss5z3lo4gipn2u
bafkreiaqv7zmg463rqkg5qah7scfiinrbfcak42vmrom7x6legl3fdoobu
bafkreibooaycl4gbhixelwrqaoxhpl2wuafss43pnhlzrdy76coyg26bn4
bafkreievmcumekxqhn6rlynz35ki3bndxum3ho5zwvszwuwf3duqtzieci
bafkreigcbr2323qcbtib7rg545ygnz5pi6dtdxpnzq27ajwht3zkv4fng4
bafkreibwnveqlszh7sqaiberutuqrqgqfayafqzob76rstu5rimcd4xx7y
bafkreiapflt2kofphe4qetsqp3pahwbgvsb4apc4hqjmgybyz2dnne3t24
bafkreifqu5f52hmumzxmyoihiuz6363j4cbs2p6npjr32f5w7izgrnc6ue
bafkreiembmkut2tsnoxewixyuw4ehuhrx4yrryyouawvfeuchcylq52c4i
bafkreig5a7frc5zgbpnace6yxr25f226q3cusbjb4h2xzhlf4jjkkvnjcy
bafkreiac4yinhsm44cbphzhntc2ipttv2qrrly6l3tchwhfueirj527mou
bafkreicoksxbq6j7lsn5w7urqr2wv5pxxaldza76xgh3vtdcnubbp3xnsm
bafkreidtomnxdzmzhbsgbcoqua3n54ax3pj66y37z5mubmqixrbxox6xk4
bafkreihac4fd62i7gdchclulkgnvfx65qdrjvoyvyzumfhsye23rncg2xe
bafkreiflknye4dbg7xdthfdeqmp2kmgwdu4owouz7h2emnlc4yykikgebm
bafkreiaagxnz4rmoq5jt4g7yr5ywlwobrifmza2eulen6kwrrgmreumzji
bafkreicdbn76fvpxcjy353xkirxofmh2jmtdwxogxk5nv3uwmzaznafaay
bafkreiby2e7elswnuyrdbtxc6oidlu5dhm535gy45tgrz2jiz6sqevc6nq
bafkreieppxpdiktwusq437dccbb5dt3x2jl5v3wainz3qxzv5doxygtrgm
bafkreigca3mbnr3mdmcju3agu4ia3n7ivtua5kaakbcpuu2ru76snbijka
bafkreig5wotfooutmcyvlxhksg7pw5nvxvpoevvxto5axz7az4om5vw7ue
bafkreies56njcoek4cff6lbwkwhcadftmmn7pkp6dfzhyx3zjwm6ygzf4u
bafkreihuwbgvfynro6lyvcz4il3rglbuj435ai6iphwujsejqfl6bebabq
bafkreicnby7l2ndnvcvdhze7rppfjlxk4g4iy2hpor4k6grbwknuxuzide
bafkreig3n446d6vjgpppxw42cts2foji5dlr7f44lml4tvcyivofvhdpka
bafkreid2m25jtovwxmrela7aik2xyzs65zxrsoashis2qpiixmhvsbxuyq
bafkreigpku75sra7t7b67lu27f3xffw7bnz6wj47v3nsipnycyiwrm5p74
bafkreiasbef4zfeknooxcfjckqsomqorklbucwa3zchbhnjj6gsvkjrpwu
bafkreientgvwukede67kfa4v2zuu5ldsxpao4h3kpc7cxiyelevo37q6hy
bafkreied3fanfpxy5edo6c46b2zhsmidgwqrffxnyiudnjv5kgn5f6eysi
bafkreidg7urwdxlneliueq6izfvnsntps7ookw5v27abdalwt2oizx6gye
bafkreibsxarkynrywfd7tt4hitkb57pffcy5jbesny57rkzdxfiukceeki
bafkreieiu56wseoadv34pdythlsrmyfnxqqh47v25ofud62du3w3nyppri
bafkreiavly3r7gd7hi6qn7c3rlqcdyng55srobnel36phdhfs52x634say
bafkreiewpo7o4ndj6zyqvdgjym4srhha623jze5zrgrdzpzbeesxtq3m4y
bafkreibv3bgpadygdkb5ck7vwdnfahc3ekvpd5477swwhj3fljhukzi5s4
bafkreic7fmcbmuf2dxjhw7ou4cd22gfq6j6rvil6pjlfgl22aybdywloq4
bafkreigixb5ptpbghwznexl3qkqtlmvsvitglvspccxqctsgv35dv4w4s4
bafkreig2bcnrio5mzza5k7tc3cr4zn3fv7e5nqh3sqldsgp3nfomprev3i
bafkreihyerg3xf4o2txmbuqdvqddmlnpkn3umjbpcp5mcysqaln6775kci
bafkreiei3w7f7m7evew4edsltup3o7jtiv5yor4shkmmt6t5rzcaavvp2y
bafkreihedwlslhbipwvdbaa5toqjh4chcrrzmyf55cdzz2ytogbiuwgrt4
bafkreic6wentmqjc6jp62xwvakpkkpwbh5bt2z3aa5avhrhi4dcll4khhi
bafkreibnk6654vbnbqlw7slrhirchtcwrfy6bx4a46hlmw3h5tfgl3um5a
bafkreiatmmhgcidnopmba3yiiomconvmofv74wef4mmg5qqywwh62ysvc4
bafkreihblhzamhenuynkl7ibhabd55z6bm52qyulrjf2jsmtvt7xe4htye
bafkreihgitg2tulxuzpsfl2cwolzas6jwgzx2tafvt7ci7pc7kdp34tply
bafkreifmqpu3p5uokzadbqagarjdj6uhn3dbsszduldcacc5rhogtrd4va
bafkreigq4xkgitgbjkrb3fvh6qqbjykvhnbxg56zettzasoxw3lcxsow2u
bafkreibuzx3vlkfyfvlvtrdlrzviumxiib6iearjm7nagamlgvsapiflgq
bafkreig5ueqohl5xyspl3qmdltaomdzsbbiam3tpsqxudnphzu3n6zooh4
bafkreibwe7fvfld4mc7tbsy6af5glo2kr5ecyrerbrga64hgqclbmxixtu
bafkreig2igm326mbubz6izzibujfuthn7oibawp5uohfgxffnjdhsxgikm
bafkreigmyjyjh4zowb6dhmmfiw4abg6e7knes3uz24a5twklkzlwmxshty
bafkreidompzd6ud3vzx7kmezepehs723lwigzypeh6f474ko7cjnn3vqqm
bafkreidirumqxc3itf32qx6mxy2p3fzioqeqfjnwff66lduow6squ6dcxm
bafkreidgwpjzqyc7z4swg2gd4x5ys6g572mau65qhmcdqhvuxl3pw5vpuu
bafkreiex7s6abrbxplrohlw2c24olsykdbymu5bqhezveqordbtnu4xih4
bafkreiddhqgjanqycadgdjve35p2jx76ozpjt4rfpuka2vui7tco7ki6jy
bafkreicsnjsyztkgpppzlwajq6myskiozleqwndqmolsi6djfoeif53f4a
bafkreihfc6rscejbe6ssuyr27sgyt4jln2bixvrutcrj74vfubafzn7eqi
bafkreihpekrosrbzhqdhhgggih4eirqggkvjwtbmwn5u7owvwusvuhl4v4
bafkreicxvymgnhxl2x2nl5tud2r2zkpemxhxwweavkuspi3uxlsqp7nmqy
bafkreiaclfv5hhm4bzrvr7n7vmwa7zbaqlm5b547zuwequxnfiidgg6enq
bafkreigoyigfwfrkoeh4y4suxdfrxz34hjjgzu7cigffydxyhvajc3bouq
bafkreibj7xr4t3gsnqqdp3pooui45epytifir7e2kzeg765pqz5lknfly4
bafkreidjtriihc6cyxpgp7u7ubg3zdsmiwrb2ah4dtbgnrsopbxc5h737u
bafkreicop75ji3ikfzhxafmuowdmt5amstbg2b5a6fbas4yldi5nnxlye4
bafkreiaiat43js2f7l7bl2m346pabc5gibaj6rnpyal4kbckr5kinkaxsi
bafkreickh77yrtjd5duri2d2uv55ngqbcl66cq6qktpp5ywuvcxkmpgd54
bafkreih7lxg3p34mhrcctu7n6b3oo5rok4n6ekn2za2bo6n4lcsjseqpn4
bafkreicntupug6koxsmqztg5j4jm2utmnjkimr7uhzcqk25mfqg5e35oum
bafkreicraw2wqmyltw5ltlhw3q22ga5miwjb2fm4tbmwwr42u5cl57mgcq
bafkreihkdbjqarjq2sw3ibohyxq25c4vqnpj2ocdpbvixumhdkkpngwqb4
bafkreickdf4xuemd2d2y2iw3bvnbqtjs3tpzjntuwa7olnmxh4q7sty3p4
bafkreianyltqsnmfrz2ybhamypvpzd6ujxztcj4r6khgoafosrgb674wpe
bafkreif52qda6kl6lsb3ky57fokvp3w4dg3jn4y4zssz6d4rmt7p3lunkq
bafkreihkmdl4xlpomn7ksa7qgc3isytio5v3dikbzafpsybytnak57k2je
bafkreidf7kbfsxmoig6yqafwlywhy74ads75zwo5344n6nm2nae2oh6dya
bafkreifkauvglwdvitpst7tvuxt7tw64j2icktlkwmaxo73bvqmcoffcha
bafkreidcawpk2mw5tdaudy7lme2c2kiuk32q5eflfs63ej7bnp4dl422ey
bafkreiboqy6dfqcnc37uz66p5ggjxp5ubluxnawn3c6ixqx6dirjfghxny
bafkreiehydn7pgouf46ofeddozvqj2cqh3wcz6p2xxh7zk3vsftsfshseq
bafkreiaducxyh6rpkhuznghw5vlrnvjng4jew7lapywlicy24mr2uu3ree
'''[1:-1].split('\n')

id = ids[-1]
base = 'https://ipfs.io/ipfs/'

proxies = { 
	"http": 'http://localhost:5000',
	"https": 'http://localhost:5000',
}

while True:
	try:
		r = requests.get(base + id, verify=False, proxies=proxies)
		id = r.text.strip()
	except:
		id = 'a' * 101
	if len(id) > 100:
		print('Retrying')
		id = ids[-1]
	else:
		print(id)
		ids.append(id)
	if not id.startswith('bafkrei'):
		break

# UlisseCTF{0n3_d4y_my_gr4ndm4_sh3_t0ld_m3_s0n_d0n7_g0_t0_m1l4n}

'''
# **Cotoletta alla bolognese: storia, ricetta e segreti della tradizione**

## Introduzione

La cotoletta alla bolognese, detta anche **"la petroniana"**, è uno dei piatti più rappresentativi della cucina tradizionale emiliana. A differenza della più nota cotoletta alla milanese, la versione bolognese si distingue per la presenza di prosciutto crudo e parmigiano reggiano fuso, il tutto condito con un tocco di **brodo di carne** che le conferisce umidità, sapore e carattere.

È un piatto sontuoso, ricco, perfetto come secondo piatto importante in un pranzo domenicale. Oggi scopriremo come realizzarlo seguendo la tradizione, ma anche alcune possibili varianti, suggerimenti di presentazione e abbinamenti con contorni e vini.

---

## **Origini e storia della cotoletta alla bolognese**

La cotoletta alla bolognese affonda le sue radici nella cucina borghese di Bologna tra la fine del XIX e l’inizio del XX secolo. Si dice sia nata per rivaleggiare con la famosa cotoletta alla milanese, ma con ingredienti più in linea con la tradizione gastronomica emiliana: il prosciutto crudo, il parmigiano reggiano e il brodo di carne.

Fu inserita nel ricettario ufficiale della **Cucina Bolognese Tradizionale** e nel 2004 l’**Accademia Italiana della Cucina**, delegazione di Bologna San Luca, ne codificò la versione ufficiale, per preservarne l’autenticità.

---

## **Ingredienti (per 4 persone)**

### Per la cotoletta

- 4 fette di **fesa di vitello** (circa 150 g ciascuna, spesse circa 1 cm)
- 2 uova
- Farina q.b.
- Pangrattato q.b. (preferibilmente di pane raffermo grattugiato in casa)
- Sale e pepe q.b.
- UlisseCTF{0n3_d4y_my_gr4ndm4_sh3_t0ld_m3_s0n_d0n7_g0_t0_m1l4n}
- Burro chiarificato (o metà burro e metà olio extravergine) per friggere

### Per la farcitura

- 4 fette di **prosciutto crudo di Parma** dolce
- 100 g di **Parmigiano Reggiano** grattugiato finemente
- Brodo di carne q.b. (circa 200 ml)
- Una noce di burro

---

## **Preparazione passo dopo passo**

### 1. **Battitura della carne**

Prendi le fette di fesa di vitello e appiattiscile con un batticarne tra due fogli di carta forno, fino a uno spessore omogeneo di circa mezzo centimetro. Questo aiuterà a rendere la carne tenera e a ottenere una cottura uniforme.

### 2. **Panatura classica**

Prepara tre piatti: uno con farina, uno con uova sbattute con un pizzico di sale, uno con pangrattato.

Passa le cotolette:

1. prima nella farina (scrollando l’eccesso),
2. poi nell’uovo sbattuto,
3. infine nel pangrattato, premendo bene con le mani per farlo aderire.

Per una panatura più spessa e croccante, puoi ripetere il passaggio nell’uovo e nel pangrattato una seconda volta.

### 3. **Frittura**

Scalda abbondante burro chiarificato (o una miscela di burro e olio EVO) in una padella ampia. Quando è caldo ma non fumante, friggi le cotolette fino a doratura, circa 3-4 minuti per lato.

Trasferiscile su carta assorbente per eliminare l’unto in eccesso. A questo punto, puoi anche prepararle in anticipo e conservarle in frigo fino al momento della gratinatura finale.

### 4. **Farcitura e gratinatura**

Adagia su ogni cotoletta una fetta di prosciutto crudo, facendo attenzione a coprire bene la superficie. Cospargi con abbondante Parmigiano Reggiano e aggiungi un mestolino di **brodo di carne caldo**, giusto per inumidire il tutto e favorire la fusione del formaggio.

Sistema le cotolette in una teglia da forno leggermente imburrata. Inforna a 200°C in modalità grill per 5-7 minuti, finché il formaggio non sarà completamente fuso e leggermente dorato.

Il brodo verrà in parte assorbito dalla cotoletta, ammorbidendo la panatura e creando un connubio perfetto tra croccantezza e cremosità.

---

## **Trucchi e consigli dello chef**

### La carne

La fesa di vitello è il taglio più adatto per questa ricetta: tenera e magra, cuoce in fretta e mantiene la sua delicatezza. Alcuni usano anche il carré disossato, ma è meno tipico.

### Il brodo

Usa un **brodo di carne fatto in casa**, ottenuto con manzo, osso con midollo, sedano, carota, cipolla, chiodi di garofano e un pizzico di sale. Niente dado: il sapore autentico dipende molto da questo ingrediente.

### Il prosciutto crudo

Deve essere dolce e non troppo stagionato, altrimenti rischia di diventare eccessivamente salato o di seccarsi in cottura. Il **crudo di Parma** o quello di Modena sono perfetti.

### Il parmigiano

Più è stagionato, più sarà saporito e tenderà a formare una crosticina dorata irresistibile. Grattugialo finemente per una fusione omogenea.

---

## **Varianti tradizionali e moderne**

### 1. **Versione "alla vecchia Bologna"**

In alcune vecchie famiglie si aggiunge un pizzico di **noce moscata** all’uovo della panatura o si spalma un velo di besciamella sotto il prosciutto per una versione ancora più sontuosa.

### 2. **Versione light**

Invece di friggere, puoi cuocere le cotolette impanate al forno con un filo d’olio, anche se il risultato sarà meno croccante. Una volta cotte, aggiungi prosciutto, parmigiano e brodo, e completa con la gratinatura.

### 3. **Senza glutine**

Usa farina di riso e pangrattato senza glutine per rendere il piatto adatto anche ai celiaci.

---

## **Contorni consigliati**

### 1. **Purè di patate**

Il più classico e delicato, perfetto per accompagnare una cotoletta così ricca.

### 2. **Erbette saltate in padella**

Bietole, spinaci o cicoria leggermente amarognole creano un bel contrasto.

### 3. **Insalata mista**

Un contorno leggero e fresco, ideale se vuoi bilanciare la grassezza del piatto.

---

## **Abbinamento vini**

Un piatto così ricco richiede un vino con corpo ma non troppo tannico. Le scelte ideali:

- **Lambrusco Grasparossa di Castelvetro DOC**: frizzante, fresco e leggermente tannico.
- **Sangiovese di Romagna Superiore**: fruttato, rotondo e con buona struttura.
- **Barbera d’Alba**: se vuoi abbinare un vino fuori regione ma sempre equilibrato.

Per chi preferisce il bianco, un **Pignoletto frizzante** dei Colli Bolognesi può sorprendere per freschezza e versatilità.

---

## **Come servire la cotoletta alla bolognese**

Impiatta la cotoletta ben calda, con il formaggio ancora filante. Aggiungi un mestolino del sughetto creatosi nella teglia per irrorare la carne. Puoi guarnire con un filo di brodo a parte e un ciuffo di prezzemolo fresco tritato, anche se non è tradizionale, dona un tocco di colore.

---

## **Conservazione**

- **In frigo**: si conserva per un paio di giorni in un contenitore ermetico. Si può riscaldare in forno statico a 180°C per 10 minuti.
- **In freezer**: puoi congelare le cotolette fritte _prima_ della gratinatura, separandole con carta forno. Al momento del consumo, lasciale scongelare, poi farcisci e gratina.

---

## **Curiosità**

- A Bologna, in alcuni ristoranti storici, la cotoletta alla bolognese è servita come “secondo piatto del giorno” in trattorie frequentate da locali e turisti.
- La versione originale prevedeva anche l’uso di **tartufo bianco** grattugiato sopra al formaggio fuso durante la stagione autunnale.
- Il nome "alla Petroniana" deriva da **San Petronio**, patrono di Bologna, come segno di rispetto per la tradizione cittadina.

---

## **Conclusione**

La cotoletta alla bolognese è molto più di una semplice variante della cotoletta: è un inno alla ricchezza gastronomica dell’Emilia, un piatto che unisce croccantezza, sapidità e morbidezza in un’unica, golosissima portata. È perfetta per chi ama i sapori decisi, la cucina di una volta, e le ricette che raccontano una storia.

Prepararla richiede attenzione, ingredienti di qualità e un po’ di amore per la tradizione. Ma il risultato ripagherà ogni sforzo: una cotoletta fondente, saporita, profumata, che sa di casa e di domenica in famiglia.

Buon appetito!
'''
