#There are three exercises, each with a separate datafile.


#1. The datafile "seminar2.txt" contains the results of a pilot study on the perception of foreign accent. 
#In this study, 9 listeners heard 18 Swedish words spoken by native and by non-native speakers (column speaker.L1). 
#The participants themselves were also either native speakers or non-native speakers 
#(column "L1" 1 = native; 0 = non-native). 

#Analyze this datafile. Specifically:

# Build a regression model that includes the interaction between speaker L1/L2 and listener L1/L2.

library(tidyverse)
library(broom)


LS = read.csv("seminar2.csv", header = T)
LS

LS %>% count(L1 , speaker.L1)

sum(is.na(LS$correct))

LS_int_mdl = lm(correct ~ L1 * speaker.L1, data = LS)

tidy(LS_int_mdl) %>% select(term, estimate)


# model with centering

LS <- mutate(LS, L1_c = L1 - mean(L1, na.rm = TRUE))


LS_int_mdl_c <- lm(correct ~ L1_c * speaker.L1, data = LS)


tidy(LS_int_mdl_c) %>% select(term, estimate)


# The regression model will have four coefficients. Explain each of the four coefficients.

# The intercept for L1 is 0.36 L1 slope is estimated to be -0.22, indicating a negative relationship between response and L1.
# Negative coefficient -0.08 shows that speakers with native accent does not affect accent perception among listeners.
# Overall, considering the slopes of listeners and speakers, it is assumed that accent perception is not affected by them in isolation,
# while the positive interaction coefficient 0.23(with or without centering) indicates that listener's accent perception is not significantly affected by 
# the speakers with native accent when producing Swedish words.


# Then test the difference in response accuracy between native and non-native speakers within the L1 listeners and within the L2 listeners.


library(tidyverse)
library(broom)


LS = read.csv("seminar2.csv", header = T)
LS

LS_mdl <- glm(correct==1 ~ L1, data= LS, family = 'binomial')

tidy(LS_mdl)
summary(LS_mdl)

select (LS, correct, L1)

table(LS$correct)
table(LS$L1)


# The intercept is -0.75 when x=0 but The slope of the L1 predictor is negative(-0.56), meaning that 
#non_native L2 listeners have a better performance in accent perception, however, this difference is 
#not significant within subjects.

# Make a barplot of the predicted proportions correct with (approximate) 95% confidence intervals.

library (ggplot2)

LS = read.csv("seminar2.csv", header = T)
LS

LS_glm <- glm(correct==1 ~ L1, data= LS, family = 'binomial')

summary(LS_glm)

table(LS$L1) 
table(LS$correct)/sum(table(LS$correct))
(xtab <- table(LS$L1,LS$correct))
(xtab/rowSums(xtab))


ggplot(data = LS) 
barplot(xtab/rowSums(xtab),beside=T,legend=T) +
  geom_errorbar(aes(ymin = -0.5619-1.96*0.3614, ymax = -0.5619 + 1.96*0.3614), width = 0.5) + 
  theme_minimal()

summary(LS_glm)
(upper.boundary= plogis(-0.5619 + 1.96*0.3614))
(lower.boundary=plogis(-0.5619-1.96*0.3614))


#2. The file Diet.csv shows weight loss in people following either one of four diets. Test whether there was an overall significant diet effect and subsequently test all the pairwise comparisons between the four diets. Make a barplot of the average weight loss per diet together with error bars representing 95% confidence intervals.

library(tidyverse)
library(broom)

wloss = read.csv("Diet.csv")
wloss 

summary(wloss)


wloss_mdl <- lm(WeightChange ~ Diet, data = wloss)

tidy(wloss_mdl)

wloss_null <- lm(WeightChange ~ 1, data = wloss)
wloss_null

# Perform model comparison:
anova(wloss_null, wloss_mdl)

# Model comparison provides the F-value 5.41 and p.value 0.001287, showing that there is an overall significant effect for 
# diets which leads to weight loss.


# Pairwise comparison

library(emmeans)
emmeans(wloss_mdl, list(pairwise ~ Diet),
        adjust = 'bonferroni')

# Standardize valence and take the absolute value:
wloss <- mutate(wloss,
                WeightChange_z = scale(WeightChange),
                AbsWeightChange = abs(WeightChange_z))
# Omnibus test:
abs_mdl <- lm(AbsWeightChange ~ Diet, data = wloss)
# Model comparison without specifying null model directly:
anova(abs_mdl)


newpreds <- tibble(Diet = sort(unique(wloss$Diet)))
newpreds

# Generate predictions:
fits <- predict(wloss_mdl, newpreds)
fits

# Standard errors for predictions:
SEs <- predict(wloss_mdl, newpreds,
               se.fit = TRUE)$se.fit
SEs

CI_tib <- tibble(fits, SEs)
CI_tib

# Compute CIs:
CI_tib <- mutate(wloss_preds,
                 LB = fits - 1.96 * SEs, # lower bound
                 UB = fits + 1.96 * SEs) # upper bound
CI_tib


wloss_preds <- predict(wloss_mdl, newpreds,
                       interval = 'confidence')
wloss_preds

# Compute CIs:
CI_tib <- mutate(wloss_preds,
                 LB = fits - 1.96 * SEs, # lower bound
                 UB = fits + 1.96 * SEs) # upper bound
CI_tib

wloss_preds <- cbind(newpreds, wloss_preds)
wloss_preds


wloss_preds %>%
  ggplot(aes(x = Diet, y = fit)) +
  geom_point(size = 4) +
  geom_errorbar(aes(ymin = lwr, ymax = upr),
                size = 1, width = 0.5) +
  ylab('weight change\n') +
  xlab('\nDiet') +
  theme_minimal() +
  theme(axis.text.x =
          element_text(face = 'bold', size = 15),
        axis.text.y =
          element_text(face = 'bold', size = 15),
        axis.title =
          element_text(face = 'bold', size = 20))
#Make a barplot of the average weight loss per diet together with error bars representing 95% confidence intervals.

library(tidyverse)
library(broom)
library(ggplot2)

wloss = read.csv("Diet.csv")
wloss


t.test(wloss$WeightChange)
mean(wloss$WeightChange)
sd(wloss$WeightChange)
se <- qt(0.975, 239)*sd(wloss$WeightChange)/sqrt(240)
se

ggplot(wloss, aes(x=Diet,y= WeightChange, fill = Diet))+
  geom_bar(stat = "summary", fun = mean) +
  geom_errorbar(aes(ymin = -8.30 - 1.96 * 1.83, ymax = -8.30 + 1.96* 1.83 ),width= 0.2)+
  theme_minimal()           

#The model results and graph suggest that the significant changes in average weight loss is caused by Atkins diet 
# while the change for three other diets is slightly different just with a decreasing trend in average weight loss 
# for Ornish, LEARN and Zone,respectively.  

# 3. The file reading.txt contains hypothetical data of the relation between phonological awareness and reading comprehension. 60 pupils from three schools were measured on these variables. 

# - Do an exploratory analysis of the relationship between phonological awareness and reading comprehension.

library("tidyverse");library("broom")

phoncomp = read.csv("readingexample.csv")
phoncomp

range(phoncomp$awareness)

phoncomp_mdl <- glm(comprehension~awareness,data=phoncomp,family="poisson")
tidy(phoncomp_mdl)

summary(phoncomp_mdl)


# Intercept value 0.03 is positive, showing that the phonological awareness has 
# positive effect on the rate of reading comprehension among students of three schools.

exp(3.50803)
exp(0.03091)


# Exponentiation analysis shows that if x = 0(if students of three schools have no phonological awareness), the proportions of reading comprehension 
# are predicted to be about 33  and increase in reading comprehension is affected by each 1 unit increase in phonological awareness.

# - estimate the effect of phonological awareness and reading comprehension for the entire dataset. 
library(tidyverse)
library(lme4)

phoncomp = read.csv("readingexample.csv")
phoncomp
summary(phoncomp)


model1 <-lmer(comprehension ~ 1 + (1|school),data=phoncomp)
summary(model)

model2 <-lmer(comprehension ~ 1 + awareness + (1|school),data=phoncomp)
summary(model2)

anova(model1, model2)

# The models comparison provides information about how adding phonological awareness as predictor has reduced the sum of squares or the 
# deviance by 7.1226. Moreover, the comparison indicates that random slope is enough to show random effects of predictors 
# regardless of the correlation between slopes and intercepts.In this respect, model1 could be a better model to estimate 
# the effect of phonological awareness and reading comprehension among the students from three schools.
 

# - Make a graph that shows the results of the analysis.

# overall graph:
ggplot(phoncomp,aes(x=awareness,y=comprehension,group=factor(school), fill=school, color=school)) + 
  geom_point() + geom_line()

# plots by school:
ggplot(phoncomp,aes(x=awareness,y=comprehension, fill=school, color=school)) + 
  geom_point() + geom_line() + facet_wrap(.~school)


# graph by students:
ggplot(phoncomp,aes(x=awareness,y=comprehension,group=factor(school),col=factor(child))) +
  geom_point() + geom_line()


# More clearly, the graph demonstrates that reading comprehension is going up with an approximately 
# general similar pattern for the students from three schools, effected by each increase 
# in phonological awareness.Although many fluctuations and much variation are observed 
# in the graph,the positive effect of the phonological awareness on reading comprehension 
# is evident among the students from three schools specifically significantly for the students 
# from the school C to consider.