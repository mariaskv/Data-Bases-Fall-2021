Μέλη Ομάδας:
1. Σκευοφύλακα Μαρία - 1115201900173
2. Λιονής Εμμανουήλ - Γεώργιος - 11152001900103


Διευρινήσεις:


* Παρόλο που τόσο o patient όσο και ο doctor ανήκουν στην ευρύτερη κατηγορία person επιλέξαμε να μην τα συνδέσουμε μεταξύ τους και να αντιμετωπίσουμε το person ως ένα πίνακα ατόμων που σχετίζονται με τον εμβολιασμό. 
* Ο πίνακας visit συνδέει τις οντότητες patient, doctor και αναπαριστά την επίσκεψη ενός ασθενή στο νοσοκομείο. Αυτό μας επιτρέπει να έχουμε απευθείας πρόσβαση στο ποιος γιατρός εξέτασε κάποιον ασθενή.
* Στον πίνακα admission υπάρχει ένα χαρακτηριστικό “symptoms” το οποίο θα μπορούσε να είναι ξεχωριστός πίνακας, προτιμήσαμε όμως να το βάλουμε σαν χαρακτηριστικό και ολα τα συμπτώματα να είναι σε μία σειρά καθώς δεν ήταν σαφής από την εκφώνηση η υλοποίηση που έπρεπε να ακολουθήσουμε σε αυτό το σημείο.
* Τα κοινά στοιχεία των Hospital, Diagnostic Center βρίσκονται μέσα στον πίνακα Center. Αυτό το κάναμε έτσι ώστε να γράφει ο προγραμματιστής μια φορά για κάθε νέο κέντρο τα στοιχεία του. Στο Diagnostic Center όμως χρειαζόμαστε μία επιπλέον πληροφορία, το email.
* Για τις εξετάσεις έχει δημιουργηθεί ένας πίνακας που αναπαριστά όλα τα είδη εξετάσεων (covid test, blood exams etc.). Αυτό επιλέχθηκε για να κρατηθούν όλες οι εξετάσεις σε ένα σημείο και για την καλύτερη διαχείριση των δεδομένων και αφέθηκε στον προγραμματιστή της βάσης η υποχρέωση να τους δώσει τίτλους. Στην περίπτωση που δεν πρόκειται για covid test και ο ΕΟΔΥ δεν αποδίδει μοναδικό κωδικό δύναται αυτή η σχέση να είναι NULL.
* Οι οντότητες ΕΟΔΥ, ΕΜΑ, ΗΔΙΚΑ έχουν αναπαρασταθεί από τρεις πίνακες που ο καθένας περιέχει μόνο ένα χαρακτηριστικό όνομα της οντότητας. Αυτό επιλέχθηκε προκειμένου να είναι ευκολότερη η αναπαράσταση των μεταξύ τους σχέσεων αλλά και των αλληλεπιδράσεων τους με τις άλλες οντότητες. Επίσης θεωρήσαμε πως αυτές οι τρεις οντότητες είναι οργανισμοί με διάφορα παραρτήματα σε διάφορες περιοχές και όχι μία ενιαία αρχή.
* Η συνεργασία μεταξύ ΕΟΔΥ και ΕΙΔΙΚΑ επιλέχθηκε να αναπαρασταθεί με την μορφή πίνακα καθώς υπονοείται από την εκφώνηση και θεωρήσαμε σωστό να αναπαρασταθεί για περισσότερη σαφήνεια. 
* Ο ΕΙΔΙΚΑ αναθέτει σε κάθε πολίτη έναν μοναδικό αριθμό ΑΜΚΑ ο οποίος έχει αντιστοιχία 1:1 με κάθε πολίτη. 
* Όσον αφορά τα εμβόλια κάθε παρτίδα εμβολίων έχει έναν μοναδικό κωδικό που του αναθέτει ο ΕΜΑ και αυτός ο κωδικός περνάει και σε κάθε μεμονωμένο εμβόλιο μέσω της παρτίδας στην οποία ανήκει. 
* Σαν vaccine θεωρούμε τόσο το είδος του εμβολίου όσο και το μεμονωμένο τεμάχιο. Αυτό γίνεται προκειμένου να αναπαρασταθεί η σχέση approve που κάνει το ΕΜΑ η οποία γίνεται μία μόνο φορά για κάθε είδος εμβολίου. Το batch_of_vaccines αναπαριστά την παρτίδα των εμβολίων που δημιουργείται κάθε φορά από το εργοστάσιο. (Πχ. κάθε μέρα μπορεί να παράγεται διαφορετικός αριθμός παρτίδων από διαφορετικές εταιρείες η καθεμία).
* Οι μεταβλητές τύπου TINYINT χρησιμοποιήθηκαν ως bool μεταβλητές προκειμένου να διαχωριστεί αν κάτι ισχύει ή όχι (πχ. Αν μια πτέρυγα είναι ΜΕΘ ή όχι).