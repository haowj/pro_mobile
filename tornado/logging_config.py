config = {
	'disable_existing_loggers': False,
	'version': 1,
	'formatters': {
		'simple': {
			'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		},
	},
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'DEBUG',
			'formatter': 'simple'
		},
		'rotating_time': {
			'class': 'logging.handlers.TimedRotatingFileHandler',
			'filename': r'E:\log\logging.log',
			'when': 'd',
			'formatter': 'simple'
		}
	},

	'loggers': {
		'': {
			'handlers': ['console', 'rotating_time'],
			'level': 'DEBUG',
		}
	}
}
