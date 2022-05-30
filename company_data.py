
validCompanies = ["sanofi","novartis","pfizer","merck","hoffmannlaroche","shire","glaxosmithkline",
"gileadsciences","daiichisankyo","boehringeringelheim", "bayerhealthcare", "abbottlaboratories",
"bristolmyerssquibb", "holleypharmaceuticals", "johnsonandjohnson", "guilinpharmaceutical", 
"elilillyandcompany", "kyorinpharmaceutical", "taishopharmaceutical", "artepharm"]

companyNames = {
    "sanofi": "Sanofi",
    "novartis": "Novartis",
    "pfizer": "Pfizer Inc.",
    "merck": "Merk & Co., Inc.",
    "hoffmannlaroche": "F. Hoffmann-La Roche LTD.",
    "shire": "Shire Pharmaceuticals",
    "glaxosmithkline": "GlaxoSmithKline LTD.",
    "gileadsciences": "Gilead Sciences, Inc.",
    "daiichisankyo": "Daiichi Sankyo",
    "boehringeringelheim": "Boehringer Ingelheim",
    "bayerhealthcare": "Bayer Healthcare",
    "abbottlaboratories": "Abbott Laboratories",
    "bristolmyerssquibb": "Bristol-Myers Squibb",
    "holleypharmaceuticals": "Chongqing Holley Pharmaceutical Co. LTD",
    "johnsonandjohnson": "Johnson and Johnson",
    "guilinpharmaceutical": "Guilin Pharmaceutical Co., LTD",
    "elilillyandcompany": "Eli Lilly and Company LTD",
    "kyorinpharmaceutical": "Kyorin Pharmaceutical Co., LTD",
    "taishopharmaceutical": "Taisho Pharmaceutical Co. LTD",
    "artepharm": "Artepharm",
}

dbNames = {
    "sanofi": "Sanofi",
    "novartis": "Novartis",
    "pfizer": "Pfizer Inc.",
    "merck": "Merck",
    "hoffmannlaroche": "F. Hoffmann-La Roche Ltd",
    "shire": "Shire Pharmaceuticals",
    "glaxosmithkline": "GlaxoSmithKline",
    "gileadsciences": "Gilead Sciences, Inc.",
    "daiichisankyo": "Daiichi Sankyo",
    "boehringeringelheim": "Boehringer Ingelheim",
    "bayerhealthcare": "Bayer Healthcare",
    "abbottlaboratories": "Abbot Laboratories",
    "bristolmyerssquibb": "Bristol-Myers Squibb",
    "holleypharmaceuticals": "Chongqing Holley Pharmaceutical Co. Ltd and Sigma Tau Industrie Farmaceutiche",
    "johnsonandjohnson": "Johnson and Johnson",
    "guilinpharmaceutical": "Guilin Pharmaceutical Co., Ltd",
    "elilillyandcompany": "Eli Lilly and Company",
    "kyorinpharmaceutical": "Kyorin Pharmaceutical Co., Ltd.",
    "taishopharmaceutical": "Taisho Pharmaceuticals",
    "artepharm": "Artepharm",
}

companyBlurbs = {
    "sanofi": '''Sanofi is a global pharmaceutical company founded in 1973, headquartered
        in Paris, France, and formed from the mergers of several companies between
        1999 and 2011. Their products fall into several therapeutic areas including:
        cardiovascular, anti-infection, diabetes, immunology, neurology, oncology,
        rare disease and general well-being (nutrition, pain, allergy). A few of their key
        products include Ambien®, Plavix®, Renagel®, and the vaccines, Fluzone®
        and Menactra®. In their effort to reduce the global disease burden Sanofi
        has: collaborated with the Drugs for Neglected Diseases Initiative to create
        the ASAQ Winthrop®, an anti-malaria drug that has enabled the treatment of
        over 450 million cases at preferential pricing since 2007, worked with national
        malaria control programs and various NGOs to develop the Schoolchildren
        against Malaria Program aimed at promoting prevention behavior in schools
        in Africa, and is currently running a clinical trial, in collaboration with the
        Medicines for Malaria Venture, to develop Ferroquine, a potential alternative
        to artemisinin-based treatments that are being increasingly resisted. In 2017,
        Sanofi reported $40.9 billion dollars in revenue and 100,000 employees in
        100 countries.''',
    "novartis": '''Novartis is a global pharmaceutical company headquartered in Basel,
        Switzerland and established in 1996 by the merger of Ciba-Geigy and
        Sandoz Laboratories. The company focuses on a range of disease areas
        including: oncology, respiratory, cardio-metabolic, neuroscience, and
        immunology/dermatology. Major products include Gilenya®, Cosentyx®
        and Gleevec®. Novartis works to expand access to medicines for malaria
        through several initiatives including a zero-profit model to malariaendemic countries that reached 43.7 million people in 2017, clinical
        trials researching two novel antimalarial drug candidates, and a renewed,
        5-year, $100 million R&D investment to help reach the WHO’s 2030
        malaria elimination targets. Novartis also expands access to medicine by
        not enforcing patents in LICs and LDCs and through the Novartis Access
        Program which treats public-sector customers with chronic illnesses for one
        USD per treatment, per month. In 2017 they had 126,000 employees in
        155 countries and a revenue of $49.1 billion.''',
    "pfizer": '''Pfizer Inc is a global pharmaceutical company headquartered in New
        York, NY and founded in 1849 by Charles Pfizer and Charles Erhart. Pfizer’s
        products delve into many therapeutic areas such as: pain management,
        respiratory, digestive, inflammation, immunology, rare disease,
        cardiovascular, oncology, and anti-infection. Major products include Lyrica®,
        Prevnar 13®, and Ibrance®. Pfizer works to reduce the disease burden with
        programs such as: the International Trachoma Initiative, co-founded in 1998
        with the Edna McConnell Clark Foundation that treated over 100 million
        people in 2017, the Diflucan Partnership Program, launched in 2000, that
        has donated over 100 million treatments for HIV-related infection, and cash
        grants/investments through the Pfizer Foundation that funds initiatives
        aimed at improving health care delivery in low and middle income
        countries. Pfizer Inc. has over 90,000 employees in over 125 countries and
        earned a revenue of approximately $52.5 billion in 2017.''',
    "merck": '''Merck & Co., Inc. is a global pharmaceutical company founded in 1891 and
        headquartered in Kenilworth, New Jersey. The company focuses their products in
        the areas of diabetes, cancer, vaccines and hospital acute care. Major drugs include
        Januvia®, Keytruda®, and Isentress®. Their research efforts focus on cancer, HIV, HPV,
        hepatitis C, cardio-metabolic disease, antibiotic-resistant infection, and Alzheimer’s
        disease. Merck attempts to make HIV medication, primarily Isentress®, accessible by
        offering pricing to countries based on disease burden and country income, licensing
        generics production, and, since 2017, making pediatric raltegravir available at zero
        profit in least-developed/low-income countries until generics become available. Their
        Institutional Business Africa unit works to ensure access to essential medicines in Africa;
        in 2015 they vaccinated one million girls in Rwanda and Uganda for HPV. In 2017, 42
        of Merck’s products were available at differential pricing to improve access in LICs and
        LDCs including Gardasil®, Atripla®, and MMR-II® and $90 million was put into patientprovider education programs. They employ approximately 69,000 people and earned a
        revenue of about $40.1 billion in 2017.''',
    "hoffmannlaroche": '''Headquartered in Switzerland, Hoffman-LaRoche is a global pharmaceutical
        company founded by Fritz Hoffmann-La Roche in 1896. They focus primarily
        on in-vitro diagnostics, cancer medication, and drugs for viral infections,
        inflammatory diseases and CNS disorders. Some of their key products include
        Herceptin®, MabThera®/Rituxan® and Perjeta®. In 1934, they became the
        first company to mass-produce synthetic vitamin C, which was branded as
        Redoxon. Roche, in collaboration with the Clinton Health Care Initiative and
        other organisations, supervise the Global Access Programme for HIV as they
        work to diagnose and treat individuals in low and middle income countries. In
        collaboration with the Medicine Patent Pool, they have made Valcyte available
        for HIV/AIDS programs at close to non-profit prices in 138 countries. They
        have several projects running that aim to improve cancer care in developing
        countries. Currently, the Swiss firm Novartis owns a third of its shares. In
        2017, Hoffman LaRoche reported revenue of about $53 billion with 93,734
        employees in more than 100 countries.''',
    "shire": '''Shire Pharmaceuticals is a global pharmaceutical company, headquartered
        in Massachusetts and founded in 1986 by a group of entrepreneurs,
        specializing in the treatment of rare diseases. They are set to be acquired by
        Takeda Pharmaceutical by the 1st half of 2019. They focus their research and
        manufacturing in the areas of: hematology, neuroscience, immunology, genetic
        diseases, internal medicine and ophthalmics. Major products include: Adderall®,
        Lialda®, and Gammagard Liquid®. Shire has programs to improve access to
        medical care focused around hemophilia including OnePath® and Shire Cares®.
        Through an agreement with the World Federation of Hemophilia they provide
        annual donations of clotting factor, donating nearly eight million units in 2017.
        Shire, in collaboration with Canada’s Access to Medicine Regime, has recently
        allowed royalty-free access to HIV/AIDS medicines for Rwanda to improve health
        and save lives in the developing world. In 2017, Shire earned a revenue of $15.16
        billion and employed approximately 23,000 workers in 100 countries.''',
    "glaxosmithkline": '''GlaxoSmithKline is a global pharmaceutical company headquartered
        in Brentford, London, and founded in 2000 after the merger of
        GlaxoWellcome and SmithKline Beecham. They focus on the manufacture
        of HIV and respiratory-related pharmaceuticals, oral health, respiratory, pain
        relief consumer healthcare products, and a broad portfolio of vaccines. Viiv
        Healthcare, majority owned by GSK, along with Pfizer Inc., is a joint-venture
        pharmaceutical company focusing on advancing care and delivering
        treatment to HIV communities. Viiv’s approach to improving access to their
        current portfolio of 12 HIV medicines involves not applying for patents
        in LDCs or LICs, voluntary licensing (royalty-free) for all least developed,
        low-income, lower-middle income, and Sub-Saharan African countries,
        and providing at-cost pricing in LDCs, LICs and SSAs (until generics are
        available), while focusing their R&D to improve HIV care and prevention.
        One GSK program, in partnership with Medicine for Malaria Ventures,
        developed a new P. vivax malaria treatment, the only new treatment for this
        strain in the past 60 years. Key GSK products include Zentel®, Malarone®
        and Tivicay®. They have nearly 100,000 employees working in over 150
        countries and a turnover of $39.7 billion in 2017.''',
    "gileadsciences": '''Gilead Sciences, Inc. is a biotechnology company founded in 1987
        by Michael Rourdan and headquartered in California that develops
        and sells pharmaceuticals. Currently, the company is highly invested in
        drugs for HIV/AIDS, respiratory conditions, cardiovascular ailments, and
        metabolic disorders. Gilead works to improve access to HIV medicine
        in low/middle income countries with tiered pricing schemes, voluntary
        licensing agreements, and financial support to HIV/AIDS programs in
        various countries. They are currently the top manufacturer of HIV drugs
        and are in the process of testing a possible cure to HIV. Some of their key
        products include Truvada®, Biktavy® and Atripla®. They have about 10,000
        employees operating in over 30 countries, and in 2017 they reported a
        revenue of approximately $26.1 billion.''',
    "daiichisankyo": '''Daiichi Sankyo is the second largest pharmaceutical company in Japan
        and was founded in 2005 by the merger of Sankyo Co. and Daiichi
        Pharmaceutical. The company is currently ranked 17th in sales worldwide
        and holds both the German biotech company, U3, and the American
        biotech company, Plexxikon. Daiichi Sankyo focuses on prescription drug
        manufacturing and research and development that focuses on oncology,
        cardiovascular-metabolics, and pain management. They have been funding
        the Global Health Innovative Technology Fund since 2013 to promote the
        development of drugs for infectious diseases in developing countries.
        Significant drugs include: Azor®, Benicar®, and Effient®. In 2017, their
        revenue was $8.48 billion dollars with operations in over 50 countries and
        over 14,400 employees.''',
    "boehringeringelheim": '''Boehringer Ingelheim is a global pharmaceutical company headquartered
        in Ingelheim, Germany, founded in 1885 by Albert Boehringer. BI
        manufactures and researches medicines for humans as well as animals. BI
        works to improve access to essential medicine by collaborating with the
        Medicine Patent Pool to waive patent rights to needed medicines, using
        tiered pricing schemes, and donating anti-retroviral drugs to increase
        access to HIV medication, such as Viramune®. They recently began an
        Access to Healthcare Strategy looking to improve access to essential
        medicines in low and middle income countries, primarily focusing on noncommunicable diseases such as diabetes and obesity. Major products
        include Aggrenox®, Flomax®, and Viramune®. The company operates in
        over 100 countries with about 50,000 employees, earning a revenue of
        $20.8 billion in 2017.''',
    "bayerhealthcare": '''The Bayer Group is a global pharmaceutical company founded in Germany in 1863 by Friedrich
        Bayer and Johann Friedrich Weskott. Bayer Healthcare strives towards innovation, health, and
        sustainability in multiple fields, including cardiology, gynecology, oncology, ophthalmology and
        hematology. They are currently working on the development of a new insecticide active
        ingredient to improve malaria control, investigating an active substance that may be effective in
        patients with river blindness, engaging in a clinical study to better dose children with Chagas’
        disease, as well as awaiting the WHO evaluation of Fluodora® Fusion, a product that can be
        used to combat insecticide resistant mosquitoes. For ten years, Bayer has been supplying WHO,
        free of charge, with two substances against Chagas’ and African sleeping sickness. Notable
        products include Aspirin®, Aleve®, Avelox®, and LifeNet®, an insecticide infused anti-
        malarial net. Bayer has nearly 100,000 employees and had a net income of approximately $40
        billion in 2017. Their group comprises 237 companies in 79 countries.''',
    "abbottlaboratories": '''Abbott Laboratories is a global pharmaceutical company headquartered
        in Illinois and founded by Dr. Wallace C. Abbott in 1888. Their products
        emphasize pain management, cardiovascular disease, nutrition, diabetes
        care, diagnostics and emerging-market pharmaceuticals. Their products for
        pancreatic enzyme replacement therapy (Creon), progesterone deficiency
        (Duphaston), and anti-vertigo medicine (Serc), lead in key emerging
        markets. In 1985, Abbott developed the world’s first HIV blood-screen test.
        Currently, Abbot is the largest manufacturer of HIV rapid tests, priding itself
        on its focus on point-of-care testing in the fight against HIV. In 2017, they
        delivered more than one billion tests.to healthcare professionals and patients
        worldwide. Other significant products include Similac and Pediasure. Abbott
        currently has over 99,000 employees across 150 countries, and their revenue in
        2017 exceeded $27.3 billion.''',
    "bristolmyerssquibb": '''Bristol-Myers Squibb, formed from the merger of Bristol-Myers and Squibb in 1989, is a global
        pharmaceutical company founded in 1858, currently headquartered in New York, NY. The
        company manufactures products in the areas of cardiovascular disease, HIV, cancer, diabetes,
        hepatitis, psychiatric disorders, and rheumatoid arthritis. They are focused on developing and
        delivering medicines that help patients with serious diseases. BMS’s Global Access Program
        improves access to three of their HIV medicines through a patent policy that allows for generic
        manufacturing and zero-profit pricing in low-income countries. Their Secure the Future®
        initiative, a branch of the Bristol-Myers Squibb foundation, works to alleviate burden from HIV
        in communities in Africa by offering different kinds of care. Some of their products include
        Videx®, Evotaz® and Zerit®. In 2017, the company’s revenue was $20.8 billion and they had
        23,700 employees.''',
    "holleypharmaceuticals": '''Holley Pharmaceuticals is an affiliate of the Chinese company Chongqing
        Holley with a manufacturing facility in California. Chongqing Holley
        advocates for corporate social responsibility to promote social well-being
        and help realize the value of life. Holley Pharmaceuticals, which established
        itself in the U.S. in 2002, is one of the world’s largest manufacturers of
        artemisinin, an antimalarial.''',
    "johnsonandjohnson": '''Johnson & Johnson is a global pharmaceutical and consumer goods company headquartered in
        New Brunswick, New Jersey, and founded by Robert, James and Edward Johnson in 1886. They
        are divided into three business segments, consumer, medical devices, and pharmaceuticals,
        focusing their medicine in six therapeutic areas: cardiovascular and metabolism, immunology,
        infectious disease and vaccines, neuroscience, oncology, and pulmonary hypertension. Major
        products include Remicade®, Aria®, and Stelara®. J&J’s Bedaquiline Access Program has
        donated bedaquiline since 2015 and is offering this MDR-TB drug at a lower, non-commercial
        cost for low-and-middle income nations in order to make it more accessible. They donate about
        200 million doses of mebendazole each year to treat worms in underserved regions. They have
        over 95 products on the Access to Medicines index, are currently running a clinical trial on a
        potential HIV preventive vaccine regimen, and have announced collaboration with IMTECH to
        discover new TB medicines. Johnson and Johnson had a revenue of $76.45 billion and
        approximately 134,000 employees, operating in over 60 countries, in 2017.''',
    "guilinpharmaceutical": '''Guilin Pharmaceutical Co., Ltd., a subsidiary of the Shanghai Fosun
        Pharmaceutical Group, is a global pharmaceutical company headquartered
        in Shanghai, China and founded in 1958. They specialize in antimalarials,
        antibiotics, and generics, including Artesun® Arsuamoon® and Artecospe®.
        Since 2006, Guilin, the largest manufacturer of artemisinin globally, has
        provided over 100 million Artesunate to malaria endemic areas, saving
        approximately 20 million lives. Guilin has approximately 1,200 employees
        and had a revenue of $124 million in 2017.''',
    "elilillyandcompany": '''Colonel Eli Lilly founded Eli Lilly and Company in 1876. Lilly, a global
        pharmaceutical company headquartered in Indiana, focuses its efforts
        in the areas of oncology, immunology, diabetes care, chronic pain,
        Alzheimer’s disease and animal health. The company maintains the Lilly
        Open Innovation Drug Discovery Program, useful for scientists researching
        various diseases including multidrug-resistant tuberculosis. It was the first
        company to mass produce the Salk polio vaccine, insulin, and Prozac®, as
        well as the first to develop capreomycin. Lilly works to improve access to
        medicine by using differential pricing schemes, waving property rights in
        least-developed countries and through donations on products delivered
        via the Lilly TruAssist program and Life for a Child. Their products are
        currently sold in nearly 125 countries and include Trulicity®, Humalog®, and
        Alimta®. The company employs about 38,000 workers and in 2017, Eli Lilly
        reported revenue of over $19.97 billion.''',
    "kyorinpharmaceutical": '''Kyorin Pharmaceutical Co., Ltd is a global pharmaceutical company founded in 1923 and
        headquartered in Tokyo, Japan. It is engaged in the manufacture and sale of prescription
        medicines, focusing on respiratory, urinary, ear, nose, and throat drugs. With a mission of
        looking to alleviate medical burden by providing innovative drugs globally, they seek to use their
        products to help better global health. Some of its key products include Mucodyne® and Kipres®.
        Kyorin originated and currently licenses gatifloxacin, a fluoroquinolone antibiotic, to various
        pharmaceutical companies. Its parent company, Kyorin Holdings Inc., reported revenue of
        $985.6 million in 2017. Kyorin Pharmaceutical Co., Ltd. employs approximately 1,670 people.''',
    "taishopharmaceutical": '''Taisho Pharmaceutical Co. is a Japanese pharmaceutical company based in Tokyo. Upon establishment in 1912, 
        the company produced over-the-counter drugs, but later moved to producing prescription drugs in addition to OTC medicines. Taisho’s company 
        mission is to contribute to society by manufacturing pharmaceutical and health care products that improve people’s health, and therefore, 
        their lives as a whole. An early focus of the company was product taste, and release of an energy drink called Lipovitan-D led to Taisho’s 
        status as an OTC field leader. This was also the first product by Taisho to be sold overseas. Taisho also produces cough suppressants, pain 
        relievers, and antibiotics. Currently, Taisho markets brands such as Vicks, Tempra, Contac and several more. Taisho Holdings Inc. reported a 
        revenue of 2.61 billion dollars for the fiscal year of 2019. Taisho Pharmaceutical reported employing 9,356 employees as of 2020.''',
    "artepharm": '''Artepharm is a modern pharmaceutical company headquartered in
        Guangzhou, China and founded in 2005. It was jointly established by
        the Guangzhou University of Traditional Chinese Medicine and the
        Guangdong New South Group, its parent company. The Guangdong
        New South Group, founded in 1994, has helped to save millions of
        lives in a joint artemisinin project centered in Africa. Artepharm, which is
        expanding to comprise the core of New South Group’s business, focuses
        on the production and research of antivirals, antimalarials, artemisinin
        and other herbal products. One of its major products is Artequick®. In the
        research and development sector, Artepharm has a resource institute which
        specializes in the production of Artemisia annua L.''',
}

reportBlurb = {
    "sanofi": '''Sanofi treats three diseases in our
model - P. falc malaria, P. vivax malaria, and DS-TB - with seven total drugs
- RIfampicin (R or RMP), Artesunate/Amodiaquine (AS + AQ), Artesunate
/ Sulfadoxine-pyrimethamine (AS + SP), Chloroquine + Primaquine
(CQ + PQ), Artesunate + Mefloquine + Primaquine (AS + MQ + PQ),
Artesunate + Amodiaquine + Primaquine (AS + AQ + PQ), and Artesunate
+ Sulfadoxine + Primaquine (AS + SP + PQ). Sanofi receives credit for
five treatments against P. falc malaria - Artesunate/Amodiaquine (AS +
AQ), Artesunate + Sulfadoxine + Primaquine (AS + SP + PQ), Artesunate
/ Sulfadoxine-pyrimethamine (AS + SP), Artesunate + Mefloquine +
Primaquine (AS + MQ + PQ), and Chloroquine + Primaquine (CQ +
PQ). These five drugs averted 9,792,177.01 of the total DALYS for P. falc
malaria, which is 43.05% of the worldwide DALYs that we estimate would
have been lost due to P. falc malaria in 2015 in the absence of effective
treatment. Sanofi’s drug portfolio placed it 2nd in terms of total averted
DALYs for P. falc malaria. Sanofi receives credit for two treatments against
P. vivax malaria - Chloroquine + Primaquine (CQ + PQ) and Artesunate
+ Amodiaquine + Primaquine (AS + AQ + PQ). These two drugs averted
370,800.53 of the total DALYS for P. vivax malaria, which is 95.08% of
the worldwide DALYs that we estimate would have been lost due to P.
vivax malaria in 2015 in the absence of effective treatment. Sanofi’s drug
portfolio placed it 1st in terms of total averted DALYs for P. vivax malaria.
Sanofi receives credit for one treatment against DS-TB - RIfampicin (R or
RMP). This one drug averted 8,470,126.91 of the total DALYS for DS-TB,
which is 25.00% of the worldwide DALYs that we estimate would have
been lost due to DS-TB in 2015 in the absence of effective treatment.
Sanofi’s drug portfolio placed it in a tie for 1st in terms of total averted
DALYs for DS-TB.''',
    "novartis": '''Novartis treats two diseases in our model - P. falc malaria and P. vivax malaria - with
one drug - Artemether-Lumefantrine (AL). Novartis receives credit for one treatment against P. falc
malaria - Artemether-Lumefantrine (AL). This one drug averted 12,918,639.54 of the total DALYS
for P. falc malaria, which is 56.81% of the worldwide DALYs that we estimate would have been lost
due to P. falc malaria in 2015 in the absence of effective treatment. Novartis’s drug portfolio placed
it 1st in terms of total averted DALYs for P. falc malaria. Novartis receives credit for one treatment
against P. vivax malaria - Artemether-Lumefantrine (AL). This one drug averted 194.46 of the total
DALYS for P. vivax malaria, which is 0.05% of the worldwide DALYs that we estimate would have
been lost due to P. vivax malaria in 2015 in the absence of effective treatment. Novartis’s drug
portfolio placed it 4th in terms of total averted DALYs for P. vivax malaria.''',
    "pfizer": '''Pfizer Inc. treats five diseases in our model - DSTB, MDR-TB, XDR-TB, P. falc malaria, and LF - with seven total drugs - Ethambutol
(E or EMB), Ethionamide (Eto), Cycloserine (Cs), p-aminosalicylic acid (PAS),
Diethylcarbamazine (DEC), Nelfinavir (NFV), and Doxycycline (D). Pfizer Inc.
receives credit for one treatment against DS-TB - Ethambutol (E or EMB). This
one drug averted 8,470,126.91 of the total DALYS for DS-TB, which is 25.00%
of the worldwide DALYs that we estimate would have been lost due to DS-TB in
2015 in the absence of effective treatment. Pfizer Inc.’s drug portfolio placed it
in a tie for 1st in terms of total averted DALYs for DS-TB. Pfizer Inc. receives credit
for three treatments against MDR-TB - Cycloserine (Cs), Ethionamide (Eto), and
p-aminosalicylic acid (PAS). These three drugs averted 1,213,914.04 of the total
DALYS for MDR-TB, which is 60.70% of the worldwide DALYs that we estimate
would have been lost due to MDR-TB in 2015 in the absence of effective treatment.
Pfizer Inc.’s drug portfolio placed it 1st in terms of total averted DALYs for MDRTB. Pfizer Inc. receives credit for one treatment against XDR-TB - Cycloserine (Cs).
This one drug averted 26,589.80 of the total DALYS for XDR-TB, which is 37.50%
of the worldwide DALYs that we estimate would have been lost due to XDR-TB in
2015 in the absence of effective treatment. Pfizer Inc.’s drug portfolio placed it
1st in terms of total averted DALYs for XDR-TB. Pfizer Inc. receives credit for one
treatment against HIV - Doxycycline (D). This one drug averted 1,579.82 of the
total DALYS for HIV, which is 0.06% of the worldwide DALYs that we estimate would
have been lost due to HIV in 2015 in the absence of effective treatment. Pfizer
Inc.’s drug portfolio placed it 8th in terms of total averted DALYs for HIV. Pfizer Inc.
receives credit for one treatment against P. falc malaria - Doxycycline (D). This one
drug averted 1579.82 of the total DALYS for P. falc malaria, which is 0.01% of the
worldwide DALYs that we estimate would have been lost due to P. falc malaria in
2015 in the absence of effective treatment. Pfizer Inc.’s drug portfolio placed it 5th
in terms of total averted DALYs for P. falc malaria. Pfizer Inc. receives credit for one
treatment against LF - Diethylcarbamazine (DEC). This one drug averted 245.39
of the total DALYS for LF, which is 4.94% of the worldwide DALYs that we estimate
would have been lost due to LF in 2015 in the absence of effective treatment. Pfizer
Inc.’s drug portfolio placed it 3rd in terms of total averted DALYs for LF.''',
    "merck": '''Merck treats seven diseases in our model - HIV, roundworm, MDR-TB, DS-TB,
whipworm, onchocersais, and LF - with four total drugs - Streptomycin (S or STR), Efavirenz
(EFV), Ivermectin (IVM), and Pyrazinamide (Z or PZA). Merck receives credit for one treatment
against HIV - Efavirenz (EFV). This one drug averted 430,899.98 of the total DALYS for HIV,
which is 16.82% of the worldwide DALYs that we estimate would have been lost due to HIV
in 2015 in the absence of effective treatment. Merck’s drug portfolio placed it 3rd in terms
of total averted DALYs for HIV. Merck receives credit for one treatment against roundworm -
Ivermectin (IVM). This one drug averted 75,097.84 of the total DALYS for roundworm, which
is 20.54% of the worldwide DALYs that we estimate would have been lost due to roundworm
in 2015 in the absence of effective treatment. Merck’s drug portfolio placed it 2nd in terms
of total averted DALYs for roundworm. Merck receives credit for two treatments against
MDR-TB - Streptomycin (S or STR) and Pyrazinamide (Z or PZA). These two drugs averted
381,162.97 of the total DALYS for MDR-TB, which is 19.06% of the worldwide DALYs that we
estimate would have been lost due to MDR-TB in 2015 in the absence of effective treatment.
Merck’s drug portfolio placed it 3rd in terms of total averted DALYs for MDR-TB. Merck
receives credit for one treatment against DS-TB - Pyrazinamide (Z or PZA). This one drug
averted 8,470,126.91 of the total DALYS for DS-TB, which is 25.00% of the worldwide DALYs
that we estimate would have been lost due to DS-TB in 2015 in the absence of effective
treatment. Merck’s drug portfolio placed it in a tie for 1st in terms of total averted DALYs for
DS-TB. Merck receives credit for one treatment against whipworm - Ivermectin (IVM). This one
drug averted 3,621.48 of the total DALYS for whipworm, which is 26.33% of the worldwide
DALYs that we estimate would have been lost due to whipworm in 2015 in the absence of
effective treatment. Merck’s drug portfolio placed it 2nd in terms of total averted DALYs for
whipworm. Merck receives credit for one treatment against onchocersais - Ivermectin (IVM).
This one drug averted 2,790.64 of the total DALYS for onchocersais, which is 100.00% of the
worldwide DALYs that we estimate would have been lost due to onchocersais in 2015 in the
absence of effective treatment. Merck’s drug portfolio placed it 1st in terms of total averted
DALYs for onchocersais. Merck receives credit for one treatment against LF - Ivermectin (IVM).
This one drug averted 2,238.64 of the total DALYS for LF, which is 45.06% of the worldwide
DALYs that we estimate would have been lost due to LF in 2015 in the absence of effective
treatment. Merck’s drug portfolio placed it 2nd in terms of total averted DALYs for LF.''',
    "hoffmannlaroche": '''F. Hoffmann-La Roche Ltd
treats one disease in our model - DS-TB - with one total drug - Isoniazid (H or INH). F.
Hoffmann-La Roche Ltd receives credit for one treatment against DS-TB - Isoniazid (H or
INH). This one drug averted 8,470,126.91 of the total DALYS for DS-TB, which is 25.00%
of the worldwide DALYs that we estimate would have been lost due to DS-TB in 2015 in
the absence of effective treatment. F. Hoffmann-La Roche Ltd’s drug portfolio placed it
in a tie for 1st in terms of total averted DALYs for DS-TB.''',
    "shire": '''Shire Pharmaceuticals treats
one disease in our model - HIV - with one total drug - Lamivudine (3TC). Shire
Pharmaceuticals receives credit for one treatment against HIV - Lamivudine (3TC).
This one drug averted 705,778.12 of the total DALYS for HIV, which is 27.54% of
the worldwide DALYs that we estimate would have been lost due to HIV in 2015 in
the absence of effective treatment. Shire Pharmaceuticals’s drug portfolio placed
it 1st in terms of total averted DALYs for HIV.''',
    "glaxosmithkline": '''GlaxoSmithKline treats six diseases in our model -
HIV, roundworm, hookworm, whipworm, LF, and P. falc malaria - with four total drugs -
Albendazole (ALB), Atovaquone + Proguanil (AT + PG), Zidovudine (AZT), and Abacavir
(ABC). GlaxoSmithKline receives credit for two treatments against HIV - Zidovudine (AZT)
and Abacavir (ABC). These two drugs averted 375,309.79 of the total DALYS for HIV,
which is 14.65% of the worldwide DALYs that we estimate would have been lost due to
HIV in 2015 in the absence of effective treatment. GlaxoSmithKline’s drug portfolio placed
it 4th in terms of total averted DALYs for HIV. GlaxoSmithKline receives credit for one
treatment against roundworm - Albendazole (ALB). This one drug averted 281,499.93
of the total DALYS for roundworm, which is 77.00% of the worldwide DALYs that we
estimate would have been lost due to roundworm in 2015 in the absence of effective
treatment. GlaxoSmithKline’s drug portfolio placed it 1st in terms of total averted DALYs
for roundworm. GlaxoSmithKline receives credit for treatments against hookworm -
Albendazole (ALB). These drugs averted 24,366.12 of the total DALYS for hookworm,
which is 87.88% of the worldwide DALYs that we estimate would have been lost due
to hookworm in 2015 in the absence of effective treatment. GlaxoSmithKline’s drug
portfolio placed it 1st in terms of total averted DALYs for hookworm. GlaxoSmithKline
receives credit for one treatment against whipworm - Albendazole (ALB). This one drug
averted 7,856.36 of the total DALYS for whipworm, which is 57.12% of the worldwide
DALYs that we estimate would have been lost due to whipworm in 2015 in the absence
of effective treatment. GlaxoSmithKline’s drug portfolio placed it 1st in terms of total
averted DALYs for whipworm. GlaxoSmithKline receives credit for one treatment against
LF - Albendazole (ALB). This one drug averted 2,484.03 of the total DALYS for LF, which
is 50.00% of the worldwide DALYs that we estimate would have been lost due to LF in
2015 in the absence of effective treatment. GlaxoSmithKline’s drug portfolio placed it 1st
in terms of total averted DALYs for LF. GlaxoSmithKline receives credit for one treatment
against P. falc malaria - Atovaquone + Proguanil (AT + PG). This one drug averted 0 of the
total DALYS for P. falc malaria, which is 0.00% of the worldwide DALYs that we estimate
would have been lost due to P. falc malaria in 2015 in the absence of effective treatment.
GlaxoSmithKline’s drug portfolio placed it 8th in terms of total averted DALYs for P. falc
malaria.''',
    "gileadsciences": '''Gilead Sciences, Inc. treats one disease
in our model - HIV - with two total drugs - Tenofovir (TDF) and Emtricitabine (FTC).
Gilead Sciences, Inc. receives credit for two treatments against HIV - Tenofovir (TDF)
and Emtricitabine (FTC). These two drugs averted 621,283.21 of the total DALYS for
HIV, which is 24.25% of the worldwide DALYs that we estimate would have been lost
due to HIV in 2015 in the absence of effective treatment. Gilead Sciences, Inc.’s drug
portfolio placed it 2nd in terms of total averted DALYs for HIV.''',
    "daiichisankyo": '''Daiichi Sankyo treats two diseases in our model - XDR-TB and MDR-TB - with two
total drugs - Levofloxacin (Lfx) and Ofloxacin (Ofx). Daiichi Sankyo receives credit for two treatments
against XDR-TB - Levofloxacin (Lfx) and Ofloxacin (Ofx). These two drugs averted 13,294.90 of the total
DALYS for XDR-TB, which is 18.75% of the worldwide DALYs that we estimate would have been lost due
to XDR-TB in 2015 in the absence of effective treatment. Daiichi Sankyo’s drug portfolio placed it 2nd in
terms of total averted DALYs for XDR-TB. Daiichi Sankyo receives credit for one treatment against MDRTB - Levofloxacin (Lfx). This one drug averted 404,638.01 of the total DALYS for MDR-TB, which is 20.23%
of the worldwide DALYs that we estimate would have been lost due to MDR-TB in 2015 in the absence
of effective treatment. Daiichi Sankyo’s drug portfolio placed it 2nd in terms of total averted DALYs for
MDR-TB.''',
    "boehringeringelheim": '''Boehringer Ingelheim treats one disease in our model -
HIV - with one total drug - Nevirapine (NVP). Boehringer Ingelheim receives credit for one treatment
against HIV - Nevirapine (NVP). This one drug averted 326,973.41 of the total DALYS for HIV, which
is 12.76% of the worldwide DALYs that we estimate would have been lost due to HIV in 2015 in the
absence of effective treatment. Boehringer Ingelheim’s drug portfolio placed it 5th in terms of total
averted DALYs for HIV.''',
    "bayerhealthcare": '''Bayer Healthcare treats three diseases in our
model - schistosomiasis, P. vivax malaria, and XDR-TB - with three total drugs - Praziquantel
(PZQ), Chloroquine (CQ), and Moxifloxacin (Mfx). Bayer Healthcare receives credit for one
treatment against schistosomiasis - Praziquantel (PZQ). This one drug averted 114,408.21
of the total DALYS for schistosomiasis, which is 100.00% of the worldwide DALYs that we
estimate would have been lost due to schistosomiasis in 2015 in the absence of effective
treatment. Bayer Healthcare’s drug portfolio placed it 1st in terms of total averted DALYs
for schistosomiasis. Bayer Healthcare receives credit for one treatment against P. vivax
malaria - Chloroquine (CQ). This one drug averted 13,781.63 of the total DALYS for P. vivax
malaria, which is 3.53% of the worldwide DALYs that we estimate would have been lost
due to P. vivax malaria in 2015 in the absence of effective treatment. Bayer Healthcare’s
drug portfolio placed it 2nd in terms of total averted DALYs for P. vivax malaria. Bayer
Healthcare receives credit for one treatment against XDR-TB - Moxifloxacin (Mfx). This one
drug averted 6,647.45 of the total DALYS for XDR-TB, which is 9.38% of the worldwide
DALYs that we estimate would have been lost due to XDR-TB in 2015 in the absence of
effective treatment. Bayer Healthcare’s drug portfolio placed it in a tie for 5th in terms of
total averted DALYs for XDR-TB.''',
    "abbottlaboratories": '''Abbot Laboratories treats one disease in our model -
HIV - with one total drug - Lopinavir / Ritonavir (LPV/r). Abbot Laboratories receives credit for
one treatment against HIV - Lopinavir / Ritonavir (LPV/r). This one drug averted 83,658.48 of
the total DALYS for HIV, which is 3.26% of the worldwide DALYs that we estimate would have
been lost due to HIV in 2015 in the absence of effective treatment. Abbot Laboratories’s drug
portfolio placed it 6th in terms of total averted DALYs for HIV''',
    "bristolmyerssquibb": '''Bristol-Myers Squibb treats two diseases
in our model - XDR-TB and HIV - with four total drugs - Amikacin (Amk), Didanosine
(ddl), Stavudine (d4t), and Atazanafir/Ritonavir (ATV/r). Bristol-Myers Squibb receives
credit for three treatments against HIV - Stavudine (d4t), Atazanafir/Ritonavir (ATV/r), and
Didanosine (ddl). These three drugs averted 18,469.09 of the total DALYS for HIV, which
is 0.72% of the worldwide DALYs that we estimate would have been lost due to HIV in
2015 in the absence of effective treatment. Bristol-Myers Squibb’s drug portfolio placed
it 7th in terms of total averted DALYs for HIV.''',
    "holleypharmaceuticals": '''Chongqing Holley Pharmaceutical Co. Ltd and Sigma Tau Industrie Farmaceutiche treats
two diseases in our model - P. falc malaria and P. vivax malaria - with one total drug -
DHA-Piperaquine (DHA-PPQ). Chongqing Holley Pharmaceutical Co. Ltd and Sigma Tau
Industrie Farmaceutiche receives credit for one treatment against P. falc malaria - DHAPiperaquine (DHA-PPQ). This one drug averted 20,715.41 of the total DALYS for P. falc
malaria, which is 0.09% of the worldwide DALYs that we estimate would have been lost
due to P. falc malaria in 2015 in the absence of effective treatment. Chongqing Holley
Pharmaceutical Co. Ltd and Sigma Tau Industrie Farmaceutiche’s drug portfolio placed it
3rd in terms of total averted DALYs for P. falc malaria. Chongqing Holley Pharmaceutical
Co. Ltd and Sigma Tau Industrie Farmaceutiche receives credit for one treatment against
P. vivax malaria - DHA-Piperaquine (DHA-PPQ). This one drug averted 5,204.12 of the
total DALYS for P. vivax malaria, which is 1.33% of the worldwide DALYs that we estimate
would have been lost due to P. vivax malaria in 2015 in the absence of effective treatment.
Chongqing Holley Pharmaceutical Co. Ltd and Sigma Tau Industrie Farmaceutiche’s drug
portfolio placed it 3rd in terms of total averted DALYs for P. vivax malaria.''',
    "johnsonandjohnson": '''Johnson and
Johnson treats three diseases in our model - roundworm, hookworm, and
whipworm - with one drug - Mebendazole (MBD). Johnson and Johnson
receives credit for one treatment against roundworm - Mebendazole (MBD).
This one drug averted 9,004.29 of the total DALYS for roundworm, which is
2.46% of the worldwide DALYs that we estimate would have been lost due
to roundworm in 2015 in the absence of effective treatment. Johnson and
Johnson’s drug portfolio placed it 3rd in terms of total averted DALYs for
roundworm. Johnson and Johnson receives credit for one treatment against
hookworm - Mebendazole (MBD). This one drug averted 3,360.12 of the
total DALYS for hookworm, which is 12.12% of the worldwide DALYs that we
estimate would have been lost due to hookworm in 2015 in the absence of
effective treatment. Johnson and Johnson’s drug portfolio placed it 2nd in
terms of total averted DALYs for hookworm. Johnson and Johnson receives
credit for one treatment against whipworm - Mebendazole (MBD). This one
drug averted 2,275.63 of the total DALYS for whipworm, which is 16.55% of
the worldwide DALYs that we estimate would have been lost due to whipworm
in 2015 in the absence of effective treatment. Johnson and Johnson’s drug
portfolio placed it 3rd in terms of total averted DALYs for whipworm.
''',
    "guilinpharmaceutical": '''Guilin Pharmaceutical Co., Ltd treats one disease in our model - P. falc malaria
- with one total drug - Artemether (AM). Guilin Pharmaceutical Co., Ltd receives
credit for one treatment against P. falc malaria - Artemether (AM). This one drug
averted 9,018.93 of the total DALYS for P. falc malaria, which is 0.04% of the
worldwide DALYs that we estimate would have been lost due to P. falc malaria
in 2015 in the absence of effective treatment. Guilin Pharmaceutical Co., Ltd’s
drug portfolio placed it 4th in terms of total averted DALYs for P. falc malaria.''',
    "elilillyandcompany": '''Eli Lilly and Company treats one disease in our model - XDR-TB
- with one total drug - Capreomycin (Cm). Eli Lilly and Company receives credit for one treatment
against XDR-TB - Capreomycin (Cm). This one drug averted 8,863.27 of the total DALYS for XDR-TB,
which is 12.50% of the worldwide DALYs that we estimate would have been lost due to XDR-TB in
2015 in the absence of effective treatment. Eli Lilly and Company’s drug portfolio placed it in a tie
for 3rd in terms of total averted DALYs for XDR-TB.''',
    "kyorinpharmaceutical": '''Kyorin Pharmaceutical Co. Ltd. treats
one disease in our model - XDR-TB - with one drug - Gatifloxacin (Gfx). Kyorin Pharmaceutical
Co., Ltd. receives credit for one treatment against XDR-TB - Gatifloxacin (Gfx). This one drug
averted 4,329.80 of the total DALYS for XDR-TB, which is 9.38% of the worldwide DALYs that
we estimate would have been lost due to XDR-TB in 2015 in the absence of effective treatment.
Kyorin Pharmaceutical Co., Ltd.’s drug portfolio placed it in a tie for 5th in terms of total averted
DALYs for XDR-TB.''',
    "taishopharmaceutical": '''Taisho
Pharmaceuticals treats one disease in our model - P. falc malaria - with one drug
- Clarithromycin (CL). Taisho Pharmaceuticals receives credit for one treatment
against P. falc malaria - Clarithromycin (CL). This one drug averted 1,299.36 of
the total DALYS for P. falc malaria, which is 0.01% of the worldwide DALYs that we
estimate would have been lost due to P. falc malaria in 2015 in the absence of
effective treatment. Taisho Pharmaceuticals’ drug portfolio placed it 6th in terms
of total averted DALYs for P. falc malaria.''',
    "artepharm": '''Artepharm treats one disease in our model - P. falc
malaria - with one drug - Artemisinin + Piperaquine (ART + PPQ). Artepharm
receives credit for one treatment against P. falc malaria - Artemisinin + Piperaquine
(ART + PPQ). This one drug averted 15.16 of the total DALYS for P. falc malaria,
which is 0.00006% of the worldwide DALYs that we estimate would have been lost
due to P. falc malaria in 2015 in the absence of effective treatment. Artepharm’s
drug portfolio placed it 7th in terms of total averted DALYs for P. falc malaria.
''',
}

compKeyDrugs = {
    "sanofi": [
                    ["ARTESUNATE-SULFADOXINEPYRIMETHAMINE (AS+SP)", 
                    '''Artesunate-Sulfadoxine-Pyrimethamine (AS+SP)
                       is an artemisinin-based combination therapy
                       recommended by the WHO as one of the primary
                        treatments for both uncomplicated and severe
                        malaria. It is generally as safe and effective AS+AQ, but
                        resistance to this combination significantly reduces its
                        efficacy in the treatment of Plasmodium vivax (P. vivax)
                        malaria. Hoechst, which later became a part of Sanofi,
                        filed a patent for AS+AP in 1988.'''],
                    ["ARTESUNATE+AMODIAQUINE(AS+AQ)", 
                    '''Artesunate+Amodiaquine (AS+AQ) is an
                        artemisinin-based combination therapy (ACT)
                        recommended by the WHO as one of the primary
                        treatments for both uncomplicated and severe
                        malaria. It is relatively safe and effective with the
                        recommended dosing and 3-day duration. The first
                        patent for AS+AQ was filed in 1988 by Hoechst
                        which is now a part of Sanofi.''']
                ],
    "novartis": [
                    ["ARTEMETHER+LUMEFANTRINE (AL)", 
                    '''Artemether+Lumefantrine (AL) is an artemisinin-based combination therapy
                        recommended by the WHO as one of the primary treatments for both uncomplicated
                        and severe malaria. It is generally as safe and effective as AS+MQ, but is more likely to
                        cause earlier relapses because lumefantrine is eliminated more rapidly than some other
                        ACTs such as mefloquine. AL was patented by Novartis in 2009.'''],
                ],   
    "pfizer": [
                    ["CYCLOSERINE (CS)", 
                    '''Cycloserine (Cs) an analogue of amino acid D-alanine,, is a Group C second-line agent
                        used in the treatment of rifampicin-resistant and multidrug-resistant tuberculosis. Cs is,
                        relative to other second-line treatments, weakly effective against TB and has a high toxicity
                        profile. Side effects include acute psychosis and seizure. In 1956 Pfizer first applied for a
                        patent for Cs.'''], 
                    ["DIETHYLCARBAMAZINE (DEC)", 
                    '''Diethylcarbamazine (Dec) is an anti-filarial drug used to treat many worm infections
                    including Onchocerciasis and Schistosomiasis. Because of adverse reactions such as fever,
                    hypotension, increased eosinophilia, proteinuria and splenomegaly, diethylcarbamazine is
                    rarely used for treatment, and must only be done so in a regulated setting, such as a hospital.
                    Diethylcarbamazine was discovered in 1947, and its mechanism of action is irreversible
                    cytotoxic effect which leads to an inhibition of the parasite motility and viability. Pfizer was its
                    most recent patent holder, but this patent has since expired.'''],
                    ["DOXYCYCLINE (D)", 
                    '''Doxycycline (D): Doxycycline is a slow-acting treatment agent, and acts as an effective prophylactic
                    against P. vivax and P. falc malaria when used in combination therapy with quinine, side effects may
                    include fever, headaches, dizziness. Doxycycline was first patented by Pfizer in 1962.'''],
                    ["ETHAMBUTOL (E)", 
                    '''Ethambutol (E) is a first line semisynthetic antibiotic used in the treatment of drug-susceptible
                    tuberculosis and as an add-on agent in drug-resistant TB. Due to its high safety profile and broad
                    antibiotic activity it is a companion drug in the core TB treatment regimen. Side effects include
                    blurred vision and gastrointestinal upset. The earliest patent for E was by the American cyanamid
                    Company in 1976 and is currently held by Pfizer.'''],
                    ["ETHIONAMIDE (ETO)", 
                    '''Ethionamide (Eto) a thioamide antibiotic, is a Group C second-line agent used in the treatment of
                    rifampicin-resistant and multidrug-resistant tuberculosis. Eto is moderately effective against TB but
                    has a high toxicity profile. Side effects include seizure and blurred vision. It was first patented by Pfizer
                    in 1959.'''],
                    ["NELFINAVIR (NFV)", 
                    '''Nelfinavir (NFV) is a widely used protease inhibitor often combined with other reverse transcriptase
                    inhibitors for the treatment of HIV, but is no longer recommended for use in the U.S. Major
                    toxicity concerns include new-onset diabetes and ketoacidosis. It was developed by Agouron
                    Pharmaceuticals and, in 1998, Agouron was sold to Warner Lambert, which later merged with Pfizer.'''],
                    ["PAS (4-AMINOSALICYLIC ACID)", 
                    '''PAS (4-aminosalicylic acid) is used as an add-on agent to treat rifampicin-resistant and multidrugresistant tuberculosis. While PAS was first developed in 1902, its antituberculosis properties were
                    not discovered until 1943. Due to its high toxicity it is rarely used and is in the WHO’s last group of
                    recommended treatment for MDR-TB, Group D3. PAS was first patented by Pfizer in 1948.'''],
                ],
    "merck": [
                    ["STREPTOMYCIN (S)", 
                    '''Streptomycin (S), an aminoglycoside antibiotic, was formerly a first line tuberculosis
                    treatment, but due to toxicity and widespread resistance it is now used as a second-line
                    injectable agent to treat rifampicin-resistant and multidrug-resistant tuberculosis. Side
                    effects include auditory and renal dysfunction. Streptomycin was patented by Merck in
                    1948.'''],
                    ["IVERMECTIN (IVM)", 
                    '''Ivermectin (Ivm) is a an anti-filarial medication used to treat parasitic onchocerciasis
                    through the gradual killing of microfilariae; because of its safety and effectiveness, it
                    is a common treatment. most common side effects include itching, fever, muscle and
                    gland swelling, aches and ocular reactions, It is manufactured by Merck under the
                    brand name Mectizan®.'''],
                    ["EFAVIRENZ (EFV)", 
                    '''Efavirenz (EFV) is an ARV drug recommended by the WHO in the treatment of HIV as
                    a part of preferred first-line regimens for children, adolescents, and adults, and for
                    children also being treated for TB. Major toxicity concerns include hepatotoxicity, CNS
                    toxicity, and hypersensitivity reactions. EFV was developed and patented by Dupont
                    Merck, which then licensed it to Bristol-Myers-Squibb.'''],
                    ["PYRAZINAMIDE (Z)", 
                    '''Pyrazinamide (Z), an analogue of nicotinamine, is a first line antibiotic used in the
                    treatment of drug-susceptible tuberculosis and as an add-on agent in treating drugresistant TB. It has a high sterilizing effect and is effective at treating tuberculosis with
                    the ability to reduce the duration of treatment by several months. Side effects include
                    gastrointestinal upset and fatigue. It was first patented by Merck & Co Inc in 1954.'''],
                ],   
    "hoffmannlaroche": [
                    ["ISONIAZID (H)", 
                    '''Isoniazid (H) is the most common front line
                    treatment for drug-susceptible tuberculosis,
                    first introduced in 1954, and is also used
                    as an add-on agent to treat multidrugresistant TB. Side effects include hepatitis and
                    gastrointestinal upset. The earliest patent for
                    Isoniazid was by Hoffman La Roche in 1952.'''],
                    ["SULFADOXINE - PYRIMETHAMINE (SP)", 
                    '''Sulfadoxine - Pyrimethamine (SP) is a combination
                    of a diamino-pyrimidine, similar in structure and
                    activity to proguanil, and a sulfonamide, known
                    to have synergistic antimalarial effects with
                    pyrimethamine. While still used to treat patients
                    with sensitivity to other antimalarial agents, due
                    to high rates of resistance and a high potential
                    hepatotoxicity, it is recommended by the WHO only
                    as a part of artemisinin-based combination therapy
                    or in intermittent preventive therapy of special risk
                    groups such as pregnant women and infants.'''],
                ],   
    "shire": [
                    ["LAMIVUDINE (3TC)", 
                    '''Lamivudine (3TC) is an ARV drug recommended by the WHO in the treatment of HIV
                    as a part of preferred first-line regimens for adults, adolescents, and children, as part
                    of the recommended regimen for children also being treated for TB, and in cases of
                    HBV coinfection. Major toxicity concerns include lactic acidosis and disorders of lipid
                    metabolism. IAF Biochem first patented 3TC, changed its name to Biochem Pharma,
                    and merged with Shire Pharmaceuticals in 2000.'''],
                ],  
    "glaxosmithkline": [
                    ["ABACAVIR (ABC)", 
                    '''Abacavir (ABC) is an ARV drug recommended by the WHO as a part of the
                    preferred first-line regimen to treat HIV in children less than 10 years old, as
                    a part of an alternative first-line regimen in adolescents, and as part of the
                    recommended regimen for children also being treated for TB. Major toxicity
                    concerns include hypersensitivity reactions. The Wellcome Foundation
                    Limited first patented Abacavir. It is now a part of GlaxoSmithKline, the
                    current patent holder.'''],
                    ["ALBENDAZOLE (ALB)", 
                    '''Albendazole (Alb) is used in many worm treatments and works by keeping the worms
                    from absorbing sugar, which causes them to starve. Adverse effects include Transient
                    gastrointestinal discomfort and headache, It was patented in 1975 by the Smithkline
                    corporation. It is on the WHO’s list of essential medicines.'''],
                    ["ATOVAQUONE-PROGUANIL (AT+PG)", 
                    '''Atovaquone-Proguanil (AT+PG) is a combination therapy used in the treatment and
                    prophylaxis of P. falciparum malaria. The WHO recommends that AT+PG be used as
                    a prophylactic drug, in combination with other antimalarials. The combination was
                    patented by GlaxoSmithKline in 1999.'''],
                    ["ZIDOVUDINE (AZT)", 
                    '''Zidovudine (AZT) is an ARV drug recommended by the WHO in the treatment of HIV
                    as a part of alternative first-line regimens for adults, adolescents, and children older
                    than three years, as a part of the preferred first-line regimen for children younger than
                    three, and in the recommended treatments for children also being treated for TB,
                    and in patients with HBV coinfection. Major toxicity concerns include severe anemia,
                    neutropenia, and lactic acidosis. The first patent for Zidovudine was filed in 1999 by
                    Glaxo, which is now a part of GlaxoSmithKline.'''],
                ],  
    "gileadsciences": [
                    ["EMTRICITABINE (FTC)", 
                    '''Emtricitabine (FTC) is an ARV drug
                    recommended by the WHO in the treatment of
                    HIV as a part of preferred first-line regimens for
                    adults and adolescents, as part of an alternative
                    first-line regimen for children, and in cases of
                    HBV coinfection. Major toxicity concerns include
                    lactic acidosis and neutropenia. It was first
                    developed by scientists at Emory University and
                    Gilead Sciences Inc paid $525 million for the
                    royalties.'''],
                    ["TENOFOVIR (TDF)", 
                    '''Tenofovir (TDF) is an ARV drug
                    recommended by the WHO in the
                    treatment of HIV as a part of preferred
                    first-line regimens for adults and
                    adolescents, as a part of alternative
                    first-line regimens for children older
                    than three years, and as part of the
                    recommended regimen in cases of HBV
                    coinfection. Major toxicity concerns
                    include chronic kidney disease, lactic
                    acidosis, and decreases in bone mineral
                    density. Tenofovir was first patented by
                    Gilead Sciences Inc.'''],
                ],  
    "daiichisankyo": [
                    ["LEVOFLOXACIN (LFX)", 
                    '''Levofloxacin (Lfx), a fluoroquinolone
                    antibiotic, is a Group A second line drug
                    used in the treatment of rifampicinresistant and multidrug-resistant
                    tuberculosis. It has a good safety profile
                    and is relatively highly effective against
                    TB. Side effects include hallucinations
                    and diarrhea. Lfx was patented by Daiichi
                    Sankyo in 2006.'''],
                    ["OFLOXACIN (OFX)", 
                    '''Ofloxacin (Ofx), a fluoroquinolone
                    antibiotic, has widely been replaced as
                    a treatment for TB by later generation
                    fluoroquinolone antibiotics. Due to its
                    toxicity, its primary use is now as an
                    ophthalmic in ear and eye drops. Ofloxacin
                    was patented by Daiichi Pharmaceutical
                    Co., Ltd. in 1980.'''],
                ],  
    "boehringeringelheim": [
                    ["NEVIRAPINE (NVP)", 
                    '''Nevirapine (NVP) is an ARV drug recommended by the WHO in the treatment of
                    HIV as a part of alternative first and second-line regimens for adults, adolescents,
                    and children. Major toxicity concerns include hepatotoxicity and hypersensitivity
                    reactions. NVP was first patented by Boehringer Ingelheim.'''],
                ],  
    "bayerhealthcare": [
                    ["CHLOROQUINE", 
                    '''Chloroquine (CQ) is an aminoquinoline recommended by the WHO as an alternative to
                    ACTs in the treatment of uncomplicated malaria in areas with chloroquine-susceptible
                    infections. Due to its good safety profile and well-documented effectiveness, it is a primary
                    treatment of uncomplicated malaria, although resistance to chloroquine is widespread. It
                    was first developed in 1934 by Hans Andersag, a researcher at Bayer.'''],
                    ["MOXIFLOXACIN", 
                    '''Moxifloxacin (Mfx): A fluoroquinolone antibiotic, is a Group A second line drug used in
                    the treatment of rifampicin-resistant and multidrug-resistant tuberculosis. It has a good
                    safety profile and is relatively highly effective against TB. Side effects include seizure and
                    gastrointestinal upset. The drug was patented by Bayer in 1997.'''],
                    ["PRAZIQUANTEL", 
                    '''Praziquantel (Pzq) is an anthelmintic used to specifically treat schistosomiasis, liver flukes,
                    and cysticercosis. it works by increasing the intra-tugument influx of Calcium which
                    leads to rapid contractions of the worm and eventually death. Common side effects
                    include abdominal discomfort, vertigo, and muscle aches. Praziquantel is on the WHO
                    list of essential medicines. It is sold under the brand name Biltricide. Praziquantel was
                    discovered by Bayer, though the patent has expired.'''],
                ],  
    "abbottlaboratories": [
                    ["LOPINAVIR/RITONAVIR (LPV/R)", 
                    '''Lopinavir/ritonavir (LPV/r) is an ARV combination drug recommended by the WHO in
                    the treatment of HIV as a part of preferred second-line regimen for adults, adolescents,
                    and children older than three years, as a part of the preferred first-line regimen for
                    children under three years old, and recommended in cases with HBV coinfection.
                    Major toxicity concerns include hepatotoxicity, pancreatitis and electrocardiographic
                    abnormalities. It was patented by Abbott Laboratories in 1996.'''],
                ],   
    "bristolmyerssquibb": [
                    ["ATAZANAVIR/RITONAVIR (ATV/R)", 
                    '''Atazanavir/Ritonavir (ATV/r) is an ARV
                    combination drug recommended by
                    the WHO as a part of preferred secondline regimens to treat HIV in adults and
                    adolescents, as part of an alternative 2ndline regimen for children, and as part of
                    the preferred 2nd line regimen when
                    there is an HBV coinfection. Major toxicity
                    concerns include jaundice, nephrolithiasis,
                    and electrocardiographic abnormalities.
                    Atazanavir/ Ritonavir was first patented
                    Bristol-Myers Squibb in 1998.'''],
                    ["AMIKACIN (AMK)", 
                    '''Amikacin (Amk), an aminoglycoside
                    antibiotic, is a second-line injectable agent
                    recommended in the treatment of rifampicinresistant and multidrug-resistant tuberculosis.
                    It is proven effective against TB and has a
                    moderate safety profile. Side effects include
                    hearing loss and damage to the kidneys. A
                    patent for Amk was issued to Bristol Myers
                    Squibb in 1973.'''],
                    ["DIDANOSINE (DDL)", 
                    '''Didanosine (ddl) is an ARV drug that is no longer
                    recommended, and should be discontinued
                    for use, by the WHO as an alternative medicine
                    in 2nd-line regimens because of toxicity, low
                    efficacy, and inconvenient dosing procedure.
                    However, it can be added as a back-up drug
                    while lacking procurement of more effective
                    ARVs. Didanosine was developed by researchers
                    in the National Cancer Institute(NCI). Due to
                    limitations as a public agency, the NCI granted
                    Bristol-Myers Squibb Co. exclusive rights to
                    market didanosine.'''],
                    ["STAVUDINE (D4T)", 
                    '''Stavudine (d4T) is an ARV drug that is no
                    longer recommended for use by the WHO
                    and should be discontinued as a part of HIV
                    treatment regimens due to mitochondrial
                    toxicity. It was first patented by Bristol Myers
                    Squibb.'''],
                ], 
    "holleypharmaceuticals": [
                    ["DIHYDROARTEMISININ-PIPERAQUINE (DHA-P;DHA+PPQ)", 
                    '''Dihydroartemisinin-Piperaquine (DHA-P;DHA+PPQ) is an artemisinin
                    combination therapy recommended by the WHO as one of the primary
                    treatments for both uncomplicated and severe malaria. It is generally as safe
                    and effective as AS+AQ, but provides a longer prophylactic effect due to its
                    longer half-life. It was developed by Sigma-Tau in partnership with Medicines
                    for Malaria Venture (MMV). In 2010, Chongqing Tonghe Pharmaceuticals Co.
                    Ltd was awarded the patent.'''],
                ],
    "johnsonandjohnson": [
                    ["MEBENDAZOLE (MBZ)", 
                    '''Mebendazole (Mbz) is an anthelmintic used to treat various worm infections. It
                    interferes with the reproduction and feeding capabilities of helminths. Adverse effects
                    include transient gastrointestinal discomfort and headache. It is marketed in the US
                    under the brand name Vermox. The drug was patented by Janssen Pharmaceuticals in
                    1972, whose parent company is Johnson and Johnson.'''],
                ],
    "guilinpharmaceutical": [
                    ["ARTESUNATE (AS)", 
                    '''Artesunate (AS) is a water-soluble
                    artemisinin derivative that can be
                    prepared in oral, rectal, intramuscular,
                    and intravenous forms. It is the most
                    recommended treatment for malaria
                    when used in combination therapy
                    and as parenteral therapy to begin
                    the treatment of severe malaria. Side
                    effects include dizziness, abdominal
                    pain and cardiac arrhythmias. A patent
                    for Artesunate was issued to Guilin
                    Pharmaceutical Co. Ltd in 1986.'''],
                    ["Artemether (AM)", 
                    '''Artemether (AM), an artemisinin
                    derivative, is recommended by the
                    WHO as an alternative to artesunate
                    when artesunate is unavailable.
                    Evidence suggests that artesunate is
                    more effective than artemether when
                    used as an intramuscular injection
                    and in parenteral therapy, although
                    artemether is preferred to quinine. It is
                    a part of one of the primary treatment
                    options for uncomplicated malaria when
                    used in combination with lumefantrine.
                    AM was first invented by Guilin in 1976.'''],
                ],
    "elilillyandcompany": [
                    ["CAPREOMYCIN (CM)", 
                    '''Capreomycin (Cm), a cyclic peptide antibiotic, is a second-line injectable agent
                    recommended in the treatment of rifampicin-resistant and multidrug-resistant
                    tuberculosis. It is proven effective against TB and has a moderate safety profile,
                    although aminoglycosides are generally favored over capreomycin. Side effects include
                    hearing loss and damage to the kidneys. Cm was patented by Eli Lilly & Co. in 2007.
                    '''],
                ],
    "kyorinpharmaceutical": [
                    ["GATIFLOXACIN (GFX)", 
                    '''Gatifloxacin (Gfx) is a quinolone antibiotic recommended by the WHO as a Group A
                    second-line agent for treatment of multidrug-resistant tuberculosis. Gfx had a good
                    safety profile and is effective against TB. However, due to adverse side effects including
                    hepatotoxicity, Gatifloxacin was withdrawn in 2006, and is currently only available as an
                    ophthalmic solution in the United States and Canada. Gfx was first patented by Kyorin
                    Pharmaceuticals in 1986.'''],
                ],
    "taishopharmaceutical": [
                    ["CLARITHROMYCIN (CL)", 
                    '''Clarithromycin (CL), a macrolide antibiotic, is no longer a WHO recommended drug
                    in the treatment of tuberculosis due to ineffectiveness, although it is sometimes
                    used in the treatment of MDR-TB and RR-TB. It is used for respiratory, soft tissue and
                    skin infections such as pneumonia and pharyngitis and other bacterial infections by
                    stopping bacterial growth. Clarithromycin was first patented by Taisho Pharmaceutical
                    in 1994.'''],
                ],
    "artepharm": [
                    ["ARTEMISININ-PIPERAQUINE (ART+PPQ)", 
                    '''Artemisinin-Piperaquine (ART+PPQ) is an artemisinin-based combination therapy
                    recommended by the WHO as one of the primary treatments for both uncomplicated
                    and severe malaria. It is generally as safe and effective as AS+AQ though there is
                    more evidence for its effectiveness in treating uncomplicated malaria in areas with
                    chloroquine-resistant P. vivax. In 2006 Artepharm Global filed a patent on ART+PQ
                    under the brandname Artequick®.'''],
                ],
}