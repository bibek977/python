letter='''  Sample Letter of Inquiry to a Foundation
Example (Medical Research Related)
<December 9. 2009>
<Mr. James M. Alfred>
<New York, NY 10154>
Dear Mr. <Alfred>:
I am writing to inquire if the Bristol-Myers Squibb Foundation would consider a
proposal from the Department of Cardiothoracic Surgery at New York University
requesting a research grant of $150,000 per year for two years, to support our research
project entitled “Calcific Aortic Stenosis: Mechanisms of Calcification and Development
of Biological Markers.” The ultimate purpose of our research is to improve the clinical
outcomes and quality of lives of patients suffering from cardiovascular diseases; this
parallels the mission of Bristol-Myers Squibb Foundation to extend and enhance human
life.
After hypertension and coronary artery disease, calcific aortic stenosis (AS) is third
most common cardiovascular disease in the Western world. With a prevalence of 3-9%,
calcific AS is also the most frequent valvular disease and the main cause for valve
replacements in patients over the age of 60. Despite the high prevalence and mortality
associated with calcific AS, there is no effective medical therapy for the disease and
little is known about the molecular mechanisms driving its pathogenesis. The aim of
our research is therefore two fold: (1) to identify proteins in patients with calcific AS
that can be used to diagnose and monitor the progression of AS, and
(2) to investigate the biological mechanism by which such proteins promote calcific AS
so that we can identify possible therapeutic targets.
This research is a collaborative effort between clinicians within the Department of
Cardiology and basic science researchers and surgeons with the Department of
Cardiothoracic Surgery at New York University. This collaboration gives us the ability
to comprehensively study the disease process of AS, from its initial diagnosis by
Cardiologists to its ultimate treatment by Surgeons. The union of the clinical expertise '''

name=input(" Enter a name : ")
date=input(' Enter date : ')
address=input(" Enter Address : ")

letter=letter.replace("<Mr. James M. Alfred>",name)
letter=letter.replace("<Alfred>",name)
letter=letter.replace("<December 9. 2009>",date)
letter=letter.replace("<New York, NY 10154>",address)

print(letter)