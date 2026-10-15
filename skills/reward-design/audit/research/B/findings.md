# Unit B — visual attention, anticipation and payoff

Research run: 2026-10-10-reward-skill, searched and checked on 2026-10-10. These findings concern where people look, how they judge visual appeal, and what they learn or remember. None of the cited studies establishes that a media technique releases dopamine in an audience. Dopamine is associated with reward prediction error, anticipation and wanting, rather than pleasure itself; an audience's dopamine response cannot be inferred from clicks, gaze, liking or recall. T1 below sometimes means a behavioural meta-analysis, not a reward-circuit measurement. Recipes are design extrapolations unless explicitly described as tested conditions; applies-to lists include plausible transfers beyond the original medium.

### B1 Use a distinctive accent against a quiet field
- Claim: A target distinguished by a basic feature such as color or orientation can be easier to find than a target requiring a combination of features. Salience depends on its surroundings, so making every element conspicuous removes the useful difference.
- Mechanism: Bottom-up visual salience and feature-based visual search; subsequent attention also depends on the viewer's task.
- Evidence tier: T2 — controlled visual-search findings, supported by the later computational and psychophysical literature reviewed by Itti and Koch.
- Sources: Anne M. Treisman and Garry Gelade (1980), “A feature-integration theory of attention,” Cognitive Psychology, 12(1), 97–136, [DOI](https://doi.org/10.1016/0010-0285(80)90005-5). Laurent Itti and Christof Koch (2001), “Computational modelling of visual attention,” Nature Reviews Neuroscience, 2, 194–203, [DOI](https://doi.org/10.1038/35058500); [opened paper](https://bpb-us-e1.wpmucdn.com/wp.nyu.edu/dist/3/7631/files/2017/10/Itti_Koch_NRN_2001.pdf).
- Applies to: slides | video | UI | infographic
- How to apply: Choose the next important object and give it a distinctive accent; keep competing marks quieter. For example, highlight the relevant bar and directly label it. Check that the same object remains identifiable without color. One accent is a design starting point, not a tested numerical limit.
- Caveats: A visual-search result is not proof of engagement, comprehension or pleasure. Crowding, task goals and learned relevance can outweigh contrast; a saliency model is not a universal eye-path predictor.
- Dark pattern risk: high — the same emphasis can promote a purchase button while making refusal or cancellation hard to notice.

### B2 Use motion onset as a brief attention cue
- Claim: An object starting to move can attract attention even when that movement does not predict the target. Ongoing movement is not equivalent to motion onset.
- Mechanism: Attentional capture by a temporal change; later inhibition of return can discourage revisiting the same location.
- Evidence tier: T2 — three controlled experiments in 2003, followed by a 2018 replication and extension with animated and physical motion.
- Sources: Richard A. Abrams and Shawn E. Christ (2003), “Motion Onset Captures Attention,” Psychological Science, 14(5), 427–432, [DOI and opened article](https://journals.sagepub.com/doi/10.1111/1467-9280.01458). Kendra C. Smith and Richard A. Abrams (2018), “Motion onset really does capture attention,” Attention, Perception, & Psychophysics, 80(7), 1775–1784, [DOI](https://doi.org/10.3758/s13414-018-1548-1); [opened abstract](https://pubmed.ncbi.nlm.nih.gov/29971749/).
- Applies to: slides | video | UI | infographic
- How to apply: Start a relevant object moving when the explanation reaches it, then let it settle. For example, move an existing dot to its new position while other dots remain still. Compare first-look location and understanding against a static version; these papers do not supply an optimal UI animation duration.
- Caveats: Some smooth-animation studies failed to reproduce capture. The 2018 study found capture could disappear when a competing new object appeared; small laboratory search tasks do not establish sustained attention to looping animation.
- Dark pattern risk: high — repeated moving distractions can pull attention away from the user's task or an important disclosure.

### B3 Faces and text can dominate a frame
- Claim: Faces and text attracted disproportionate gaze in natural-image viewing, including when participants were asked to avoid them. A face in a thumbnail is therefore a plausible attention cue, but this study did not test thumbnail click-through rates.
- Mechanism: Social and semantic relevance in visual attention, beyond low-level contrast alone.
- Evidence tier: T3 — one eye-tracking study with viewing and search tasks; the thumbnail application is an extrapolation.
- Sources: Moran Cerf, E. Paxon Frady and Christof Koch (2009), “Faces and text attract gaze independent of the task: Experimental data and computer model,” Journal of Vision, 9(12), Article 10, 1–15, [DOI](https://doi.org/10.1167/9.12.10); [opened Caltech record and abstract](https://authors.library.caltech.edu/records/m51f6-vk333).
- Applies to: slides | video | UI | infographic
- How to apply: Include a face when the person is central to the message; position the key text where it can be read at the delivered size. Test thumbnails at actual thumbnail scale. Remove decorative portraits when viewers must first inspect a chart or control.
- Caveats: The reported 16.6-fold face and 11.1-fold text gaze differences were relative to size- and position-normalized regions in this task, not expected gains in clicks. Gaze is not agreement, liking or retention; reading and face relevance vary by audience.
- Dark pattern risk: high — an emotional face or provocative caption can capture attention while misrepresenting the content.

### B4 Point a character's gaze toward the next object
- Claim: People respond faster to targets on the side another person's eyes indicate. Gaze direction can guide attention.
- Mechanism: Social attentional orienting, including covert attention.
- Evidence tier: T1 — meta-analysis of 423 gaze-cueing effects, supported by an original controlled experiment.
- Sources: Kate T. McKay, Sarah A. Grainger, Sarah P. Coundouris, Daniel P. Skorich, Louise H. Phillips and Julie D. Henry (2021), “Visual attentional orienting by eye gaze: A meta-analytic review of the gaze-cueing effect,” Psychological Bulletin, 147(12), 1269–1289, [DOI](https://doi.org/10.1037/bul0000353); [opened abstract](https://pubmed.ncbi.nlm.nih.gov/35404635/). Chris K. Friesen and Alan Kingstone (1998), “The eyes have it! Reflexive orienting is triggered by nonpredictive gaze,” Psychonomic Bulletin & Review, 5, 490–495, [opened article](https://link.springer.com/article/10.3758/BF03208827).
- Applies to: slides | video | UI | infographic
- How to apply: Position the relevant object along the pictured person's gaze direction. Add a label; test whether viewers locate it correctly.
- Caveats: Timing, task and facial expression moderate the effect. Laboratory response speed does not establish conversion or learning gains.
- Dark pattern risk: low — relevant guidance; higher if it directs attention toward a misleading action.

### B5 Make a change surprising relative to an established pattern
- Claim: In a computational analysis of people watching video, events that changed the model's expectations predicted gaze better than several salience and novelty measures. Mere rarity is not the same as surprise relative to prior expectations.
- Mechanism: Bayesian surprise: change from prior to posterior beliefs in a sensory model; not a measured dopamine reward prediction error.
- Evidence tier: T3 — gaze-model comparison using eight observers, with four viewing each clip, rather than a randomized test of a media-design recipe.
- Sources: Laurent Itti and Pierre Baldi (2009), “Bayesian surprise attracts human attention,” Vision Research, 49(10), 1295–1306, [DOI](https://doi.org/10.1016/j.visres.2008.09.007); [opened paper](https://cseweb.ucsd.edu/classes/fa09/cse258a/papers/itti-baldi-2009.pdf).
- Applies to: slides | video | UI | infographic
- How to apply: Establish a legible pattern, then change the feature that carries the point: for example, show a run of similarly sized bars before revealing an outlier. Explain the exception immediately. This semantic storytelling recipe extends a low-level sensory model and needs testing.
- Caveats: The often-cited 72% describes gaze shifts toward above-average-surprise locations in this dataset. It is not a 72% engagement lift. Eight observers and many gaze shifts do not constitute a large human sample; continuous randomness may provide no useful expectation to revise.
- Dark pattern risk: high — repeated unexplained shocks or deceptive reveals can sustain checking without delivering useful information.

### B6 First impressions can form within 50 milliseconds
- Claim: Participants gave consistent visual-appeal ratings after website screenshots shown for only 50 milliseconds. This is an aesthetic first impression, not a deadline for understanding a page or deciding to leave it.
- Mechanism: Rapid extraction of global visual properties and aesthetic appraisal.
- Evidence tier: T2 — repeated controlled exposure experiments in Lindgaard and colleagues, with independent rapid-judgment evidence from Tuch and colleagues.
- Sources: Gitte Lindgaard, Gary Fernandes, Cathy Dudek and J. Brown (2006), “Attention web designers: You have 50 milliseconds to make a good first impression!”, Behaviour & Information Technology, 25(2), 115–126, [DOI](https://doi.org/10.1080/01449290500330448); [opened author-posted paper](https://www.researchgate.net/profile/Gitte-Lindgaard-2/publication/220208334_Attention_web_designers_You_have_50_milliseconds_to_make_a_good_first_impression_Behaviour_and_Information_Technology_252_115-126/links/0fcfd5100e703e957e000000/Attention-web-designers-You-have-50-milliseconds-to-make-a-good-first-impression-Behaviour-and-Information-Technology-252-115-126.pdf). Alexandre N. Tuch, Eva E. Presslaber, Markus Stoecklin, Klaus Opwis and Javier A. Bargas-Avila (2012), “The role of visual complexity and prototypicality regarding first impression of websites: Working towards understanding aesthetic judgments,” International Journal of Human-Computer Studies, 70(11), 794–811, [opened author record](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/).
- Applies to: slides | video | UI | infographic
- How to apply: Review the whole frame before polishing details: overall grouping, density and recognizable structure should support the intended impression. A brief screenshot comparison can test appeal; follow it with an unrestricted task test. The 50 ms exposure is a study condition, not recommended display time.
- Caveats: Screenshots and appeal ratings do not test navigation, comprehension or real-world abandonment. A readable slide must remain visible long enough for its content; this evidence does not support “you have only 50 ms to communicate everything.”
- Dark pattern risk: low — visual polish is useful, but can lend unwarranted credibility to weak claims.

### B7 Balance visual complexity with familiar structure
- Claim: Low-complexity, highly prototypical website screenshots were judged appealing in Tuch's experiments. Reinecke's larger dataset also linked complexity and colorfulness to appeal, with preferences varying across viewers.
- Mechanism: Processing ease and recognition of familiar interface categories; these are plausible explanations, not directly isolated neural mechanisms.
- Evidence tier: T3 — feature associations in a large screenshot-rating dataset, complemented by controlled short-exposure studies; not proof that simplification always improves usability.
- Sources: Alexandre N. Tuch, Eva E. Presslaber, Markus Stoecklin, Klaus Opwis and Javier A. Bargas-Avila (2012), “The role of visual complexity and prototypicality regarding first impression of websites: Working towards understanding aesthetic judgments,” International Journal of Human-Computer Studies, 70(11), 794–811, [opened record](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/). Katharina Reinecke, Tom Yeh, Luke Miratrix, Rahmatri Mardiko, Yuechen Zhao, Jenny Liu and Krzysztof Z. Gajos (2013), “Predicting users' first impressions of website aesthetics with a quantification of perceived visual complexity and colorfulness,” Proceedings of CHI, 2049–2058, [DOI](https://doi.org/10.1145/2470654.2481281); [opened paper](https://iis.seas.harvard.edu/papers/2013/reinecke13aesthetics.pdf).
- Applies to: slides | video | UI | infographic
- How to apply: Preserve recognizable navigation and chart conventions while removing competing decoration. Compare variants that differ in density without deleting necessary information. Reinecke collected ratings from 548 volunteers across 450 websites; appeal judgments used 500 ms exposure.
- Caveats: The websites were not a random sample of the web. Initial appeal is not long-term usefulness; demographic differences argue against a universal minimalist template. Novelty may still be appropriate when users can recognize the underlying task.
- Dark pattern risk: low — familiar structures can help users, but can also make an unfamiliar or deceptive service seem trustworthy.

### B8 Make the intended interpretation easy to perceive
- Claim: Increasing perceptual fluency increased positive aesthetic judgments in experiments using matching primes, figure-ground contrast and presentation duration. Ease of seeing can contribute to liking.
- Mechanism: Processing fluency and attribution of that ease to the object being judged.
- Evidence tier: T3 — one paper with three controlled experiments, rather than a large replication or meta-analysis.
- Sources: Rolf Reber, Piotr Winkielman and Norbert Schwarz (1998), “Effects of Perceptual Fluency on Affective Judgments,” Psychological Science, 9(1), 45–48, [DOI and opened article](https://journals.sagepub.com/doi/10.1111/1467-9280.00008).
- Applies to: slides | video | UI | infographic
- How to apply: Separate figure from background, keep the mapping between label and object consistent, and give viewers enough time to resolve the image. Test legibility before treating extra decoration as a source of delight. The paper's manipulations establish a fluency effect, not a specific font-size or exposure-time prescription.
- Caveats: Prettiness ratings do not show understanding, truth or reward chemistry. Simple or familiar is not always the aesthetic goal; an expert may value complexity. The mechanism is not a warrant to remove useful detail.
- Dark pattern risk: high — fluent presentation can make unsupported claims feel more acceptable or credible.

### B9 Attractive interfaces can feel easier to use
- Claim: Attractive interfaces can receive higher perceived-usability ratings before and after use. The aesthetic-usability effect concerns perception; it does not guarantee that a task is easier or that errors decrease.
- Mechanism: Aesthetic halo and expectations influencing subjective judgments.
- Evidence tier: T2 — converging controlled interface experiments across two research groups.
- Sources: Noam Tractinsky, A. S. Katz and D. Ikar (2000), “What is beautiful is usable,” Interacting with Computers, 13(2), 127–145, [DOI](https://doi.org/10.1016/S0953-5438(00)00031-X); [opened author record](https://cris.bgu.ac.il/en/publications/what-is-beautiful-is-usable-2/). Andreas Sonderegger and Juergen Sauer (2010), “The influence of design aesthetics in usability testing: Effects on user performance and perceived usability,” Applied Ergonomics, 41(3), 403–410, [DOI](https://doi.org/10.1016/j.apergo.2009.09.002); [opened abstract](https://pubmed.ncbi.nlm.nih.gov/19892317/).
- Applies to: UI | slides | infographic
- How to apply: Polish alignment, spacing and visual consistency, then measure task completion, mistakes and subjective ease separately. In a comparison, hold the task and functionality constant while changing appearance. Extend the finding to a presentation only as a hypothesis about perceived ease.
- Caveats: Sonderegger and Sauer also observed a performance benefit in their particular phone task; this does not make appearance a substitute for usability testing. Their sample was adolescent. Device, exposure and user population limit generalization.
- Dark pattern risk: high — aesthetic trust can conceal a confusing workflow, unreliable service or unwanted commitment.

### B10 Color arousal involves saturation and brightness as well as hue
- Claim: In a controlled color-display experiment, brighter and more saturated colors were associated with greater self-rated arousal; red was rated more arousing than blue or green. This is narrower than “all warm colors excite everyone.”
- Mechanism: Subjective arousal and autonomic response to visual stimulation; not measured dopamine or pleasure.
- Evidence tier: T3 — one factorial experiment with 62 participants, self-ratings, skin conductance and heart rate.
- Sources: Lisa Wilms and Daniel Oberfeld (2018), “Color and emotion: effects of hue, saturation, and brightness,” Psychological Research, 82, 896–914, [DOI](https://doi.org/10.1007/s00426-017-0880-8); [opened paper](https://www.staff.uni-mainz.de/oberfeld/downloads/Wilms-Oberfeld2018_Article_ColorAndEmotionEffectsOfHueSat.pdf).
- Applies to: slides | video | UI | infographic
- How to apply: Treat a saturated accent as an arousal hypothesis to test, alongside brightness and context. Compare hue variants at similar saturation and brightness. The experiment used 27 chromatic and 3 achromatic stimuli viewed for 30 seconds each; that is not a recommended duration or a tested palette for a slide.
- Caveats: Hue did not significantly affect skin-conductance amplitude, although saturation and brightness did. Arousal is not positive emotion. Isolated color fields, limited hues and one population do not establish cross-cultural media effects or a general warm-versus-cool law.
- Dark pattern risk: low — higher if exaggerated warning colors manufacture urgency or anxiety.

### B11 Myth: red focuses people and blue makes them creative
- Claim: A popular reading of color-priming research says red reliably improves detail-focused work and blue reliably improves creativity. That interpretation is too broad for a design rule.
- Mechanism: Proposed learned color associations activating avoidance or approach motivation; distinct from basic visual salience.
- Evidence tier: T2 — original controlled studies plus a larger direct replication that failed on the initial anagram-priming task.
- Sources: Ravi Mehta and Rui (Juliet) Zhu (2009), “Blue or red? Exploring the effect of color on cognitive task performances,” Science, 323(5918), 1226–1229, [DOI](https://doi.org/10.1126/science.1169144); [searched primary abstract](https://pubmed.ncbi.nlm.nih.gov/19197022/). Kenneth M. Steele (2014), “Failure to replicate the Mehta and Zhu (2009) color-priming effect on anagram solution times,” Psychonomic Bulletin & Review, 21, 771–776, [DOI](https://doi.org/10.3758/s13423-013-0548-3); [opened paper](https://www.appstate.edu/~steelekm/documents/Steele2014-Color-M%26Z.pdf). Andrew J. Elliot and Markus A. Maier (2014), “Color Psychology: Effects of Perceiving Color on Psychological Functioning in Humans,” Annual Review of Psychology, 65, 95–120, [opened review](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-010213-115035).
- Applies to: slides | video | UI | infographic
- How to apply: Choose colors for legibility, grouping, established local meaning and audience preference. If a palette is meant to improve performance, test that actual task with the intended users; do not prescribe red for analytical slides and blue for brainstorming from this priming claim.
- Caveats: Steele used the original colors, instructions and anagrams with 263 participants versus 69 originally. The predicted interaction did not reproduce. This challenges that experiment and its proposed process, not every red/blue finding or all color effects; cultural and task boundaries remain important.
- Dark pattern risk: low — the main risk is unsupported persuasion advice presented as reliable science.

### B12 Ask for a prediction before revealing the data
- Claim: Asking people to make graphical predictions and then compare them with observed data improved recall and comprehension in controlled visualization experiments. The reveal has a learning purpose when viewers can inspect and explain the difference.
- Mechanism: Prior-knowledge activation, prediction comparison and self-explanation; anticipation is a design inference, not a measured dopamine response.
- Evidence tier: T2 — a controlled main study recruiting 378 participants, with partial replications using other datasets in the same paper.
- Sources: Yea-Seul Kim, Katharina Reinecke and Jessica Hullman (2017), “Explaining the Gap: Visualizing One's Predictions Improves Recall and Comprehension of Data,” Proceedings of CHI, [DOI](https://doi.org/10.1145/3025453.3025592); [opened paper](https://users.eecs.northwestern.edu/~jhullman/explaining_the_gap.pdf); [opened author record](https://idl.uw.edu/papers/explaining-the-gap).
- Applies to: slides | video | UI | infographic | live talk
- How to apply: Show axes and group labels, ask viewers to place or sketch their expected values, reveal the observed values on the same scale, and ask them to explain the gap. A live talk can use a vote or sketch; a video can offer a pause prompt. Those live/video adaptations were not directly tested.
- Caveats: Prediction, feedback and self-explanation are different components, and effects varied by presentation modality. Immediate recall after a distractor task is not long-term retention. Do not delay safety-critical information or make an incorrect prediction socially humiliating.
- Dark pattern risk: low — higher if the reveal cherry-picks data or hides uncertainty to manufacture a dramatic reversal.

### B13 Reveal optional detail on demand
- Claim: Progressive disclosure places important, common options first and exposes advanced or rare options when requested. It can support a staged explanation, but withholding essential information is not a useful payoff.
- Mechanism: Prioritization, reduced initial complexity and user control; curiosity is a possible application, not established by this source.
- Evidence tier: T4 — practitioner guidance without a controlled experiment reported in the cited article.
- Sources: Jakob Nielsen (2006), “Progressive Disclosure,” Nielsen Norman Group, December 3, [opened article](https://www.nngroup.com/articles/progressive-disclosure/).
- Applies to: UI | slides | video | infographic
- How to apply: Put the main comparison and conclusion on the initial view; use an explicit “Show method” or “More detail” control for supporting material. For a presentation, reveal supporting evidence as it becomes relevant and finish with an integrated view. Nielsen recommends generally avoiding more than two disclosure levels; this is craft guidance.
- Caveats: Extra navigation can slow experts, bury relationships or hide options. UI disclosure and a timed cinematic reveal are different techniques. Price, consequences, required steps and the evidence needed to interpret a chart should be visible when the decision is made.
- Dark pattern risk: high — hiding fees, consent consequences or cancellation behind extra layers is deceptive disclosure.

### B14 A recognizable visual object can provide a memory hook
- Claim: Visualizations containing human-recognizable objects were more memorable in a recognition task. Some less common visualization types were also more memorable than common charts; memorable does not automatically mean comprehensible.
- Mechanism: Visual distinctiveness and semantic memory cues.
- Evidence tier: T3 — experimentally measured recognition, with correlational associations between features of existing charts and memorability.
- Sources: Michelle A. Borkin, Azalea A. Vo, Zoya Bylinskii, Phillip Isola, Shashank Sunkavalli, Aude Oliva and Hanspeter Pfister (2013), “What Makes a Visualization Memorable?”, IEEE Transactions on Visualization and Computer Graphics, 19(12), 2306–2315, [opened paper](https://vcg.seas.harvard.edu/publications/20130101-what-makes-a-visualization-memorable/paper); [opened author record](https://vcg.seas.harvard.edu/publications/20130101-what-makes-a-visualization-memorable).
- Applies to: slides | video | infographic | UI
- How to apply: Add a recognizable object tied to the subject, such as a relevant product silhouette beside a sales comparison, without distorting quantitative marks. Test both later recognition of the graphic and recall of its message. Use a familiar chart form when accurate comparison is the priority.
- Caveats: The corpus contained 2,070 charts; memorability was measured for a subset, not all 2,070. Feature associations do not prove that adding clip art causes better memory. Recognition of the picture alone is not recall of values, causality or the conclusion.
- Dark pattern risk: low — higher if memorable imagery displaces or misrepresents the quantitative evidence.

### B15 State the chart's message in the title and annotations
- Claim: Titles and supporting text attracted attention and contributed to recall of visualization messages. A memorable image can carry a message when the text and visual evidence reinforce each other.
- Mechanism: Semantic encoding, verbal-visual integration and multiple retrieval cues.
- Evidence tier: T3 — one study of 393 visualizations, eye movements from 33 participants and thousands of participant descriptions; chart features were not all randomized.
- Sources: Michelle A. Borkin, Zoya Bylinskii, Nam Wook Kim, Constance May Bainbridge, Chelsea S. Yeh, Daniel Borkin, Hanspeter Pfister and Aude Oliva (2016), “Beyond Memorability: Visualization Recognition and Recall,” IEEE Transactions on Visualization and Computer Graphics, 22(1), 519–528, [DOI](https://doi.org/10.1109/TVCG.2015.2467732); [opened paper](https://vcg.seas.harvard.edu/publications/20150101-beyond-memorability-visualization-recognition-and-recall/paper).
- Applies to: slides | video | infographic | UI
- How to apply: Replace a topic-only title such as “Quarterly sales” with a supported takeaway such as “Sales rose mainly in the final quarter.” Annotate the relevant values and keep the full chart available. After viewing, ask readers to describe the message without seeing the title.
- Caveats: Message redundancy here is not permission to duplicate long narration as dense on-screen text. Titles can bias interpretation; express uncertainty and avoid claiming causes the data cannot establish. The study supports associations, not a guaranteed uplift from a title rewrite.
- Dark pattern risk: high — a forceful headline can implant a conclusion that the chart does not support.

### B16 Signal the relevant element and its relationship
- Claim: Cues identifying relevant content or text-picture correspondences improve learning on average. Attention guidance can help viewers find the evidence needed for the explanation.
- Mechanism: Selective attention, reduced search and integration effort.
- Evidence tier: T1 — two meta-analyses of multimedia signaling.
- Sources: Sascha Schneider, Maik Beege, Steve Nebel and Günter Daniel Rey (2018), “A meta-analysis of how signaling affects learning with media,” Educational Research Review, 23, 1–24, [DOI](https://doi.org/10.1016/j.edurev.2017.11.001); [searched publisher abstract](https://www.sciencedirect.com/science/article/abs/pii/S1747938X17300581); [opened author publication record](https://www.tu-chemnitz.de/phil/imf/psyler/publikationen.php.en). Juliane Richter, Katharina Scheiter and Alexander Eitel (2016), “Signaling text-picture relations in multimedia learning: A comprehensive meta-analysis,” Educational Research Review, 17, 19–36, [DOI](https://doi.org/10.1016/j.edurev.2015.12.003); [opened repository record](https://publikationen.uni-tuebingen.de/xmlui/handle/10900/75800).
- Applies to: slides | video | UI | infographic
- How to apply: Highlight the explained component and match its label to the same cue. Remove obsolete highlights as the explanation advances.
- Caveats: Schneider reported retention g = 0.53 and transfer g = 0.33. Richter found a smaller benefit and moderation by prior knowledge; Schneider did not. Learning effects do not prove entertainment or dopamine effects.
- Dark pattern risk: low — higher if cues emphasize favorable evidence while concealing contrary evidence.

### B17 Segment a complex visual explanation into meaningful steps
- Claim: Meaningful segments improve retention and transfer compared with continuous multimedia instruction on average. Segmentation can also reduce reported cognitive load while increasing learning time.
- Mechanism: Chunking, time for processing and, in some formats, control over pace.
- Evidence tier: T1 — meta-analysis of 56 investigations and 88 pairwise comparisons.
- Sources: Günter Daniel Rey, Maik Beege, Steve Nebel, Maria Wirzberger, Tobias H. Schmitt and Sascha Schneider (2019), “A Meta-Analysis of the Segmenting Effect,” Educational Psychology Review, 31, 389–419, [DOI](https://doi.org/10.1007/s10648-018-9456-4); [opened paper](https://maria-wirzberger.de/wp-content/uploads/2019/01/Rey2019_Article_AMeta-analysisOfTheSegmentingE.pdf).
- Applies to: slides | video | UI | infographic | live talk
- How to apply: Divide a process at meaningful state changes; let each step complete before introducing the next relationship. Provide pause, replay or next-step controls where possible, and finish with an overview connecting the steps. There is no universal seconds-per-step rule in this synthesis.
- Caveats: Reported retention and transfer effects were small to medium. More learning time can explain part of the benefit; segmentation is not evidence that audiences enjoy artificial delays. Over-segmenting a simple task can add friction and obscure the whole.
- Dark pattern risk: low — higher if unnecessary stages force extra clicks or delay access to an answer.

### B18 Keep explanatory labels near what they explain
- Claim: Learning improves when related words and pictures are spatially integrated rather than separated. A viewer should not have to repeatedly search between a diagram and a remote explanation.
- Mechanism: Reduced spatial split attention and mental integration effort.
- Evidence tier: T1 — meta-analysis of 58 independent comparisons involving 2,426 participants; overall learning effect g = 0.63.
- Sources: Noah L. Schroeder and Ada T. Cenkci (2018), “Spatial Contiguity and Spatial Split-Attention Effects in Multimedia Learning Environments: a Meta-Analysis,” Educational Psychology Review, 30, 679–701, [opened article and DOI](https://link.springer.com/article/10.1007/s10648-018-9435-9).
- Applies to: slides | video | UI | infographic
- How to apply: Put short labels beside the relevant marks or diagram components, with connecting lines only when needed. Move explanatory text into the plotting area when it can remain legible. Check the delivered mobile or projected size; keep labels from covering the evidence.
- Caveats: These are learning outcomes, not measured liking. Much of the research used short instructional episodes. Integration can become clutter when there are many long labels; do not replace all legends or descriptions mechanically.
- Dark pattern risk: none — when used to clarify relationships without suppressing relevant information.

### B19 Counter-finding: seductive details can hurt learning
- Claim: Interesting but irrelevant pictures, stories or other material can impair learning of the core explanation. Making a lesson more entertaining does not necessarily improve retention or transfer.
- Mechanism: Proposed distraction, competition for processing resources and interference with coherent organization; the precise causal account remains disputed.
- Evidence tier: T1 — meta-analysis of the seductive-details effect, including variation across instructional designs.
- Sources: NarayanKripa Sundararajan and Olusola O. Adesope (2020), “Keep it Coherent: A Meta-Analysis of the Seductive Details Effect,” Educational Psychology Review, 32, 707–734, [opened article and DOI](https://link.springer.com/article/10.1007/s10648-020-09522-4).
- Applies to: slides | video | infographic | live talk
- How to apply: For every striking image or joke, state which idea it helps viewers understand. If it has no instructional role, remove it from the explanation or place it after the learning task. Test recall and application alongside enjoyment.
- Caveats: Effects vary with delivery format, pacing, language, subject and the comparison condition. This does not mean relevant illustrations, enjoyable examples or all decoration are harmful. A memory hook tied to the message is different from an unrelated spectacle.
- Dark pattern risk: low — higher if irrelevant spectacle distracts from missing evidence or important qualifications.

### B20 Animate correspondence when a chart changes
- Claim: Carefully designed animated transitions can improve tracking and some judgments of change between statistical graphics. They can show that an object persists while its position or representation changes.
- Mechanism: Object correspondence, visual continuity and reduced change blindness.
- Evidence tier: T3 — one paper with two controlled experiments using the same 24 participants.
- Sources: Jeffrey Heer and George G. Robertson (2007), “Animated Transitions in Statistical Data Graphics,” IEEE Transactions on Visualization and Computer Graphics, 13(6), 1240–1247, [DOI](https://doi.org/10.1109/TVCG.2007.70539); [opened paper](https://sites.stat.columbia.edu/gelman/communication/HeerRobertson2007.pdf).
- Applies to: slides | video | UI | infographic
- How to apply: Preserve object identity, axes and scale where possible. Separate a complicated change into understandable stages rather than moving everything simultaneously. The experiments used 1.25-second tracking transitions and 2-second change-estimation transitions; for staged scatterplots the authors recommended about one second per stage, rather than half a second.
- Caveats: Those durations belong to their tasks, not every interface. Staging could worsen tracking when stages were too fast, although participants preferred it and change estimation was not significantly better in that comparison. Animation should not distort magnitudes or replace access to the final static chart.
- Dark pattern risk: low — higher if smooth movement makes a misleading scale change or manipulated comparison harder to notice.

### B21 Myth: animation automatically improves comprehension
- Claim: A common design belief is that moving pictures teach better simply because they are engaging. Evidence supports some instructional animations, not a universal advantage for motion.
- Mechanism: Depiction of change or procedure versus transient-information load; attention and learning are distinct outcomes.
- Evidence tier: T1 — meta-analysis comparing instructional animation with static pictures, interpreted alongside an earlier critical review.
- Sources: Tim N. Höffler and Detlev Leutner (2007), “Instructional animation versus static pictures: A meta-analysis,” Learning and Instruction, 17(6), 722–738, [DOI](https://doi.org/10.1016/j.learninstruc.2007.09.013); [opened author-institute abstract](https://www.leibniz-ipn.de/en/research/publications/instructional-animation-versus-static-pictures-a-meta-analysis). Barbara Tversky, Julie Bauer Morrison and Mireille Bétrancourt (2002), “Animation: can it facilitate?”, International Journal of Human-Computer Studies, 57(4), 247–262, [DOI](https://doi.org/10.1006/ijhc.2002.1017); [opened paper](https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf).
- Applies to: slides | video | UI | infographic
- How to apply: Animate a meaningful transformation, such as how a mechanism moves, and provide pause/replay plus a stable diagram. Prefer static comparisons when viewers must inspect several values simultaneously. Compare versions containing the same information before attributing any gain to animation.
- Caveats: The meta-analysis found mean d = 0.37 across 26 studies and 76 comparisons, with larger benefits for procedural-motor knowledge. The earlier review identified confounds from extra information and interactivity. Decorative motion does not inherit the benefit of representational animation.
- Dark pattern risk: low — higher when motion creates an impression of sophistication while making evidence harder to inspect.

### B22 Make micro-interaction feedback explain the result
- Claim: Small interface responses can tell users that an action registered and what state changed. This is a practical feedback pattern, not evidence that a celebratory animation produces a dopamine hit.
- Mechanism: Action-outcome feedback, reduced uncertainty and perceived control; pleasure is a possible user response, not established by the cited guidance.
- Evidence tier: T4 — practitioner framework and examples without controlled effect estimates.
- Sources: Dan Saffer (2013), Microinteractions: Designing with Details, O'Reilly Media, [opened publisher page and contents](https://www.oreilly.com/library/view/microinteractions/9781449342760/).
- Applies to: UI | video
- How to apply: Define the trigger, rules, feedback and any loop. For “Save,” acknowledge the press, indicate progress if needed, then show an unambiguous saved state; a brief transition can connect the states. Pair an animated check with readable status text and provide a reduced-motion alternative. No universal millisecond duration is claimed here.
- Caveats: The source supports a craft framework, not a measured retention, conversion or time-perception effect. Repeated ornamental responses may burden frequent actions; feedback must match actual success rather than play before completion.
- Dark pattern risk: high — celebratory feedback can reinforce compulsive checking, or falsely suggest that an incomplete action succeeded.

### B23 Build a hierarchy, then test the actual entry point
- Claim: A visual hierarchy model that largely favored element size predicted webpage entry points poorly. Position and distinctiveness mattered, so “make it biggest and everyone sees it first” is unreliable.
- Mechanism: Interaction of spatial expectations, visual salience and search goals.
- Evidence tier: T3 — one paper with two eye-tracking studies, including a first study with 20 undergraduates.
- Sources: Jeremiah D. Still (2018), “Web page visual hierarchy: Examining Faraday's guidelines for entry points,” Computers in Human Behavior, 84, 352–359, [DOI](https://doi.org/10.1016/j.chb.2018.03.014); [searched and retrieved author paper](https://www.psychofdesign.com/jeremiah/Still_2018.pdf).
- Applies to: UI | slides | video | infographic
- How to apply: State what viewers should inspect first, second and third. Adjust placement, distinctive styling and competing content, then ask target users what they noticed first and test whether they find the intended element. These checks are a design application; they do not reproduce an eye-tracking experiment.
- Caveats: This challenges a particular Faraday model, not every use of size or hierarchy. The small, largely English-speaking university sample and static webpage tasks limit transfer to other scripts, slides and moving scenes. A predicted eye path remains a hypothesis until tested.
- Dark pattern risk: high — hierarchy can make preferred choices prominent while demoting equally legitimate alternatives.

### B24 Myth: everyone scans every design in an F or Z pattern
- Claim: The F-shaped scanning pattern is often presented as a universal law for placing content. The original research organization explicitly says F is only one of several patterns and that design can change scanning behavior; it does not establish a universal Z path either.
- Mechanism: Task-driven scanning, text formatting and reading direction rather than a fixed biological route.
- Evidence tier: T4 — practitioner reporting of field eye-tracking observations, without a controlled universal-pattern test in the article.
- Sources: Kara Pernice (2017; reviewed August 19, 2026), “F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile),” Nielsen Norman Group, [opened article](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/?swcfpc=1).
- Applies to: UI | slides | infographic
- How to apply: Use informative headings, short groups and clear labels that support the actual task. Put essential information where users expect to find it, and test the delivered layout in its reading language. Treat F/Z sketches as hypotheses, not a grid every composition must follow.
- Caveats: F scanning is associated with particular text-heavy, weakly formatted pages and may omit important content. Other patterns include heading-led scanning. Right-to-left reading can mirror the pattern; aggregate heatmaps do not describe every individual's scanpath.
- Dark pattern risk: low — higher if a presumed “unseen” region is used to bury qualifications or adverse terms.

### B25 Vary film rhythm without prescribing a universal shot length
- Claim: Hollywood films became more temporally structured across neighboring shot lengths in an analysis of 150 films released from 1935 to 2005. The authors proposed that patterns approaching 1/f might help organize attention; they did not experimentally prove an ideal cutting rate.
- Mechanism: Proposed temporal attention coordination and narrative pacing; not directly measured reward prediction error.
- Evidence tier: T3 — descriptive, correlational analysis of films rather than a randomized audience-attention experiment.
- Sources: James E. Cutting, Jordan E. DeLong and Christine E. Nothelfer (2010), “Attention and the Evolution of Hollywood Film,” Psychological Science, 21(3), [DOI](https://doi.org/10.1177/0956797610361679); [opened paper](https://jordandelong.com/pubs/2010/AttentionEvolution.pdf).
- Applies to: video | live talk
- How to apply: Plan shot changes around meaningful narrative beats and vary the rhythm across a sequence. Allow longer inspection for a chart or unfamiliar scene; shorten shots when the content can still be understood. That recipe is craft inference from descriptive evidence, not a tested seconds-per-shot formula.
- Caveats: Historical popularity, editing trends and spectral similarity cannot establish causation or audience entrainment. The corpus is Hollywood film, not short instructional video. The study does not support “cut every three seconds,” “faster always holds attention” or direct transfer to slide-change timing.
- Dark pattern risk: low — higher if rapid cutting prevents viewers from inspecting contradictory evidence or important text.
