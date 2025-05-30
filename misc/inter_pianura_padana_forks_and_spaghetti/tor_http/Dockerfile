FROM alpine:3.20.3@sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d AS POLIPO_BUILDER

WORKDIR /tmp

RUN apk add --no-cache --virtual .build-deps alpine-sdk && \
	git clone --depth 1 --single-branch https://github.com/jech/polipo.git polipo && \
    cd /tmp/polipo && \
    make

FROM alpine:3.20.3@sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d

RUN apk --update --no-cache add tor \
	&& rm -rf /var/cache/apk/*

COPY --from=POLIPO_BUILDER /tmp/polipo/polipo /usr/bin/polipo
COPY ./torrc /etc/torrc
COPY ./entry.sh /tmp/entry.sh

RUN mkdir -p /var/cache/polipo /usr/share/polipo/www

USER "tor"

WORKDIR "/var/lib/tor"

EXPOSE 5000

ENTRYPOINT [ "/tmp/entry.sh" ]
