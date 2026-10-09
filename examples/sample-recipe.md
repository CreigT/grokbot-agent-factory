# Agent recipe

name: quote-followup
one_line: Turn an open cleaning quote into a plain follow-up note the owner can send.
owner: CreigT
company: Creignificent LLC

## Problem

Open quotes sit with no next step written down.

## User

Creignificent LLC owner. Sends the note after reading it.

## Inputs

- business name
- quote amount
- service

## Outputs

- a short follow-up note
- a checklist: sent, replied, booked

## Allowed tools

- write the note in the page
- no email send until the owner copies it

## Forbidden

- auto-send email
- invent a price

## Guardrails

- owner reviews before send
- no customer list stored

## Files to build

- README.md
- index.html
- config.js

## Deploy

Vercel Other, no build.

## Done when

- page builds a note from the three inputs
- nothing is sent automatically

## Notes

Sample only. Paste your own recipe to build the real agent.
