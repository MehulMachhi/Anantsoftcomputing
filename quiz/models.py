from django.db import models

# Create your models here.
class Survey(models.Model):
    AGE_GROUP_CHOICES = [
        ('UNDER_18', 'Under 18'),
        ('18_24', '18-24'),
        ('25_34', '25-34'),
        ('35_44', '35-44'),
        ('45_54', '45-54'),
        ('55_64', '55-64'),
        ('65_ABOVE', '65 and Above'),
    ]
    
    LOCATION_CHOICES = [
        ('URBAN', 'Urban'),
        ('SEMI_URBAN', 'Semi-Urban'),
        ('RURAL', 'Rural'),
    ]
    
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES, null=True,blank=True)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=True,blank=True)
    gender_identity = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True,blank=True)
    state_union_territory = models.CharField(max_length=100, null=True,blank=True)

    EDUCATION_CHOICES = [
        ('NO_FORMAL_EDUCATION', 'No Formal Education'),
        ('PRIMARY_EDUCATION', 'Primary Education'),
        ('SECONDARY_EDUCATION', 'Secondary Education'),
        ('HIGHER_SECONDARY_EDUCATION', 'Higher Secondary Education'),
        ('BACHELORS_DEGREE', 'Bachelors Degree'),
        ('MASTERS_OR_HIGHER', 'Masters Degree or Higher'),
    ]

    FAMILIARITY_CHOICES = [
        ('VERY_FAMILIAR', 'Very Familiar'),
        ('SOMEWHAT_FAMILIAR', 'Somewhat Familiar'),
        ('NOT_VERY_FAMILIAR', 'Not Very Familiar'),
        ('NOT_AT_ALL_FAMILIAR', 'Not at All Familiar'),
    ]

    VIOLENCE_FORMS_CHOICES = [
        ('PHYSICAL_ASSAULT', 'Physical Assault (e.g., hitting, kicking, pushing)'),
        ('SEXUAL_ASSAULT', 'Sexual Assault or Rape'),
        ('VERBAL_ABUSE', 'Verbal Abuse or Name-calling'),
        ('CONTROLLING_BEHAVIOR', 'Controlling Behavior (e.g., isolating from friends/family, controlling finances)'),
        ('STALKING', 'Stalking or Persistent Unwanted Attention'),
        ('ONLINE_HARASSMENT', 'Online Harassment or Cyberbullying'),
        ('EMOTIONAL_MANIPULATION', 'Emotional Manipulation or Gaslighting'),
        ('FORCED_MARRIAGE', 'Forced Marriage or Honor-based Violence'),
        ('REPRODUCTIVE_COERCION', 'Reproductive Coercion (Forcing Pregnancy or Abortion)'),
        ('DENIAL_OF_EDUCATION', 'Denial of Education or Employment Opportunities'),
    ]

    education_level = models.CharField(max_length=50, choices=EDUCATION_CHOICES, blank=True, null=True)
    familiarity_with_violence = models.CharField(max_length=50, choices=FAMILIARITY_CHOICES, blank=True, null=True)
    witnessed_violence = models.CharField(max_length=50, choices=[('YES', 'Yes'), ('NO', 'No'), ('PREFER_NOT_TO_SAY', 'Prefer not to say')], blank=True, null=True)
    forms_of_violence = models.CharField(max_length=50, choices=VIOLENCE_FORMS_CHOICES, blank=True, null=True)

    COMMONNESS_CHOICES = [
        ('VERY_COMMON', 'Very Common'),
        ('SOMEWHAT_COMMON', 'Somewhat Common'),
        ('NOT_VERY_COMMON', 'Not Very Common'),
        ('NOT_AT_ALL_COMMON', 'Not At All Common'),
        ('UNSURE', 'Unsure'),
    ]

    LOCATION_CHOICES = [
        ('AT_HOME', 'At Home'),
        ('IN_PUBLIC_SPACES', 'In Public Spaces'),
        ('AT_WORK', 'At Work'),
        ('IN_EDUCATIONAL_INSTITUTIONS', 'In Educational Institutions'),
    ]

    PREVALENCE_CHOICES = [
        ('VERY_HIGH', 'Very High'),
        ('HIGH', 'High'),
        ('MODERATE', 'Moderate'),
        ('LOW', 'Low'),
        ('VERY_LOW', 'Very Low'),
        ('UNSURE', 'Unsure'),
    ]

    UNDERREPORTED_CHOICES = [
        ('RAPE', 'Rape'),
        ('SEXUAL_ASSAULT', 'Sexual Assault'),
        ('UNWANTED_TOUCHING', 'Unwanted Touching or Groping'),
        ('FORCED_KISSING', 'Forced Kissing'),
        ('SHARING_IMAGES', 'Sharing Intimate Images Without Consent'),
        ('COERCION', 'Coercion Into Sexual Acts'),
    ]

    commonness_physical_violence = models.CharField(
        max_length=20,
        choices=COMMONNESS_CHOICES,
        verbose_name="In your opinion, how common is physical violence against women in your community?",
        null=True, blank=True
    )
    physical_violence_location = models.CharField(
        max_length=30,
        choices=LOCATION_CHOICES,
        verbose_name="Where do you think physical violence against women most commonly occurs?",
        null=True, blank=True
    )
    sexual_violence_prevalence = models.CharField(
        max_length=20,
        choices=PREVALENCE_CHOICES,
        verbose_name="How would you rate the prevalence of sexual violence against women in your community?",
        null=True, blank=True
    )
    most_underreported_form = models.CharField(
        max_length=30,
        choices=UNDERREPORTED_CHOICES,
        verbose_name="Which form of sexual violence do you think is most underreported?",
        null=True, blank=True
    )

    BARRIER_CHOICES = [
        ('FEAR_RETALIATION', 'Fear of Retaliation'),
        ('SHAME_STIGMA', 'Shame or Stigma'),
        ('LACK_TRUST_AUTHORITIES', 'Lack of Trust in Authorities'),
        ('FEAR_NOT_BELIEVED', 'Fear of Not Being Believed'),
        ('LACK_AWARENESS', 'Lack of Awareness of Rights and Resources'),
    ]

    EMOTIONAL_ABUSE_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('UNSURE', 'Unsure'),
    ]

    EMOTIONAL_ABUSE_TYPE_CHOICES = [
        ('NAME_CALLING', 'Name-Calling or Insulting'),
        ('CONSTANT_CRITICISM', 'Constant Criticism'),
        ('HUMILIATION', 'Humiliation in Public or Private'),
        ('GASLIGHTING', 'Gaslighting'),
        ('THREATS', 'Threats'),
        ('ISOLATION', 'Isolation from Friends and Family'),
    ]

    CYBER_VIOLENCE_PREVALENCE_CHOICES = [
        ('VERY_PREVALENT', 'Very Prevalent'),
        ('SOMEWHAT_PREVALENT', 'Somewhat Prevalent'),
        ('NOT_VERY_PREVALENT', 'Not Very Prevalent'),
        ('NOT_AT_ALL_PREVALENT', 'Not At All Prevalent'),
        ('UNSURE', 'Unsure'),
    ]

    barrier_reporting = models.CharField(
        max_length=50,
        choices=BARRIER_CHOICES,
        verbose_name="What is the biggest barrier to reporting sexual violence?",
        null=True, blank=True
    )
    emotional_abuse_recognition = models.CharField(
        max_length=10,
        choices=EMOTIONAL_ABUSE_CHOICES,
        verbose_name="Do you think emotional/psychological abuse is taken as seriously as physical violence?",
        null=True, blank=True
    )
    most_common_emotional_abuse = models.CharField(
        max_length=30,
        choices=EMOTIONAL_ABUSE_TYPE_CHOICES,
        verbose_name="Which form of emotional/psychological abuse do you think is most common?",
        null=True, blank=True
    )
    cyber_violence_prevalence = models.CharField(
        max_length=20,
        choices=CYBER_VIOLENCE_PREVALENCE_CHOICES,
        verbose_name="How prevalent do you think cyber violence is against women?",
        null=True, blank=True
    )

    CYBER_VIOLENCE_CHOICES = [
        ('online_harassment', 'Online Harassment or Bullying'),
        ('impersonation', 'Impersonation on Social Media'),
        ('revenge_porn', 'Revenge Porn'),
        ('doxxing', 'Doxxing'),
    ]

    RESPONSE_ACTION_CHOICES = [
        ('intervene_directly', 'Intervene Directly'),
        ('call_authorities', 'Call the Authorities'),
        ('offer_support', 'Offer Support to the Victim Afterwards'),
        ('nothing', 'Nothing, Out of Fear or Uncertainty'),
    ]

    AWARENESS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    most_harmful_cyber_violence = models.CharField(
        max_length=50, choices=CYBER_VIOLENCE_CHOICES, verbose_name="Which form of cyber violence do you think is most harmful?", 
        null=True, blank=True
    )
    response_to_violence = models.CharField(
        max_length=50, choices=RESPONSE_ACTION_CHOICES, verbose_name="If you witnessed violence against a woman, what would you most likely do?",
        null=True, blank=True
    )
    awareness_of_resources = models.CharField(
        max_length=10, choices=AWARENESS_CHOICES, verbose_name="Are you aware of any local resources or organizations that support women experiencing violence?",
        null=True, blank=True
    )

    