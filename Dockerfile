FROM python:3

WORKDIR /workdir

COPY adventure-game/* guess-the-number/* hangman/* mad-libs-generator/* rolling-dice/* entrypoint.sh ./

RUN ["chmod", "+x", "./entrypoint.sh"]

ENTRYPOINT "./entrypoint.sh"
