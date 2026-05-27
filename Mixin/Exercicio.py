from Log import logfileMixin, logprintMixin

lp = logprintMixin()
lp.log_error('nao')
lp.log_success('sim')
lf = logfileMixin()
lf.log_error('nao mesmo')
lf.log_success('sim mesmo')


