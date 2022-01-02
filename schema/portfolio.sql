CREATE TABLE "user" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "email" varchar,
  "password" varchar
);

CREATE TABLE "about" (
  "name" varchar,
  "designation" varchar,
  "phone" phone,
  "email" email,
  "github" url,
  "linkedin" url,
  "location" varchar,
  "objective" varchar DEFAULT ''
);

CREATE TABLE "experience" (
  "designation" varchar,
  "company_name" varchar,
  "start_year" integer,
  "end_year" integer,
  "description" varchar,
  "location" varchar
);

CREATE TABLE "education" (
  "school_name" varchar,
  "grade" float,
  "out_of" integer,
  "degree" varchar,
  "start_year" int,
  "end_year" integer,
  "description" varchar DEFAULT null
);

CREATE TABLE "certification" (
  "certification_name" varchar,
  "by" varchar,
  "expire_year" varchar DEFAULT '',
  "url" url,
  "description" varchar DEFAULT null
);

CREATE TABLE "projects" (
  "project_name" varchar,
  "description" varchar,
  "url" url
);

CREATE TABLE "skills" (
  "skill_type" varchar,
  "skill_name" varchar
);
