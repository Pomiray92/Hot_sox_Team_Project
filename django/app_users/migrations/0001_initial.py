# Generated by Django 3.2 on 2023-02-12 16:24

import cloudinary.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("info_about", models.TextField(blank=True)),
                ("info_birthday", models.DateField(default=django.utils.timezone.now)),
                (
                    "info_gender",
                    models.CharField(
                        choices=[
                            ("1", "Female"),
                            ("2", "Male"),
                            ("3", "Non-Binary"),
                            ("4", "Shoelace"),
                            ("5", "Snail"),
                            ("6", "Unicorn"),
                            ("7", "Prefer not to say"),
                            ("8", "None of your business!"),
                        ],
                        max_length=10,
                    ),
                ),
                ("location_city", models.CharField(max_length=255)),
                ("location_latitude", models.FloatField(blank=True, null=True)),
                ("location_longitude", models.FloatField(blank=True, null=True)),
                ("notification", models.BooleanField(default=True)),
                (
                    "social_instagram",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "social_facebook",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "social_twitter",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "social_spotify",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Sock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("info_joining_date", models.DateField(auto_now_add=True)),
                (
                    "info_name",
                    models.CharField(
                        help_text="What is the socks name?", max_length=255
                    ),
                ),
                (
                    "info_about",
                    models.TextField(
                        blank=True, help_text="Insert sock's story in here."
                    ),
                ),
                (
                    "info_color",
                    models.CharField(
                        choices=[
                            ("1", "Black"),
                            ("2", "Grey"),
                            ("3", "White"),
                            ("4", "Red"),
                            ("5", "Green"),
                            ("6", "Yellow"),
                            ("7", "Blue"),
                            ("8", "Purple"),
                            ("9", "Orange"),
                            ("10", "Multicolor"),
                        ],
                        help_text="Select dominant color.",
                        max_length=10,
                    ),
                ),
                (
                    "info_fabric",
                    models.CharField(
                        choices=[
                            ("1", "Wool"),
                            ("2", "Cotton"),
                            ("3", "Polyester"),
                            ("4", "Bamboo"),
                            ("5", "Silk"),
                            ("6", "Nylon"),
                            ("7", "Unknown"),
                        ],
                        help_text="Select main fabric",
                        max_length=20,
                    ),
                ),
                (
                    "info_fabric_thickness",
                    models.CharField(
                        choices=[
                            ("1", "Fishnets"),
                            ("2", "Nylon thin"),
                            ("3", "Fashion victim"),
                            ("4", "Summer type"),
                            ("5", "Winter type"),
                            ("6", "Cushioned Cozy one"),
                            ("7", "Double battery powered self warming one"),
                        ],
                        help_text="Select main fabric",
                        max_length=20,
                    ),
                ),
                (
                    "info_brand",
                    models.CharField(
                        choices=[
                            ("1", "Adidas"),
                            ("2", "Puma"),
                            ("3", "Nike"),
                            ("4", "D&G"),
                            ("5", "Gucci"),
                            ("6", "Aldi"),
                            ("7", "From'ma'grandma"),
                            ("8", "Stolen"),
                            ("9", "Odd socks"),
                            ("10", "Hot socks"),
                            ("11", "Converse"),
                            ("12", "Pierre Cardin"),
                            ("13", "One Euro Shop"),
                        ],
                        help_text="Select the brand.",
                        max_length=30,
                    ),
                ),
                (
                    "info_type",
                    models.CharField(
                        choices=[
                            ("1", "Toe Socks"),
                            ("2", "Invisible"),
                            ("3", "Ankle"),
                            ("4", "Crew"),
                            ("5", "Mid-Calf"),
                            ("6", "Calf"),
                            ("7", "Knee-High"),
                            ("8", "Toe less"),
                            ("9", "Ga'ma knitted socks"),
                        ],
                        help_text="Select the type.",
                        max_length=20,
                    ),
                ),
                (
                    "info_size",
                    models.CharField(
                        choices=[
                            ("1", "25-31"),
                            ("2", "32-36"),
                            ("3", "37-40"),
                            ("4", "41-45"),
                            ("5", "46-47"),
                            ("6", "47+"),
                            ("7", "Big Foot"),
                        ],
                        help_text="Select the size.",
                        max_length=20,
                    ),
                ),
                (
                    "info_age",
                    models.PositiveSmallIntegerField(help_text="How old is the sock?"),
                ),
                (
                    "info_separation_date",
                    models.DateField(
                        default=django.utils.timezone.now, help_text="Lonely since?"
                    ),
                ),
                (
                    "info_condition",
                    models.CharField(
                        choices=[
                            ("1", "Brand new"),
                            ("2", "Fairly used"),
                            ("3", "Sunday best"),
                            ("4", "Well loved"),
                            ("5", "One of a kind"),
                            ("6", "Sporty"),
                            ("7", "Stained"),
                            ("8", "Overused"),
                            ("9", "Colorless but still going."),
                            ("10", "Involuntary Toesocks"),
                            ("11", "Lost and found"),
                            ("12", "Rescued from trash"),
                        ],
                        help_text="Select the condition of the sock.",
                        max_length=50,
                    ),
                ),
                (
                    "info_holes",
                    models.PositiveSmallIntegerField(
                        help_text="How many holes has the sock?"
                    ),
                ),
                (
                    "info_kilometers",
                    models.PositiveSmallIntegerField(
                        help_text="How many kilometers has the sock walked?"
                    ),
                ),
                (
                    "info_inoutdoor",
                    models.CharField(
                        choices=[
                            ("1", "Indoor Sock"),
                            ("2", "Outdoor Sock"),
                            ("3", "Love-live Sock"),
                            ("4", "Gym Sock"),
                            ("5", "Las Vegas Sock"),
                            ("6", "Sleeping Sock"),
                            ("7", "Japanese vendor maschine Sock"),
                            ("8", "Netflix'n'Chill Sock"),
                            ("9", "2-week Festival Sock"),
                        ],
                        help_text="Select the main environment of the sock.",
                        max_length=20,
                    ),
                ),
                (
                    "info_washed",
                    models.PositiveSmallIntegerField(
                        help_text="How often washed per month?"
                    ),
                ),
                (
                    "info_special",
                    models.CharField(
                        help_text="Description of a special interest of the sock.",
                        max_length=250,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sock",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfilePicture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="profile picture"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_picture",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserMatch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chatroom_uuid", models.UUIDField()),
                (
                    "other",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matched",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="him",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SockProfilePicture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="profile picture"
                    ),
                ),
                (
                    "sock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_picture",
                        to="app_users.sock",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SockLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dislike",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dislike",
                        to="app_users.sock",
                    ),
                ),
                (
                    "like",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="like",
                        to="app_users.sock",
                    ),
                ),
                (
                    "sock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="me",
                        to="app_users.sock",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MessageMail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("sent_date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mail",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MessageChat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=255)),
                ("sent_date", models.DateTimeField(auto_now_add=True)),
                ("seen_date", models.DateTimeField(blank=True, null=True)),
                (
                    "other",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_receiving",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_sending",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
