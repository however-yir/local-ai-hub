import os


DEFAULT_PROJECT_NAME = 'Open WebUI'
DEFAULT_PROJECT_DESCRIPTION = (
    'A self-hosted AI workspace for private assistants, local model orchestration, and team productivity.'
)
DEFAULT_PROJECT_REPOSITORY_URL = 'https://github.com/open-webui/open-webui'
DEFAULT_PROJECT_RELEASES_API_URL = 'https://api.github.com/repos/open-webui/open-webui/releases/latest'
DEFAULT_PROJECT_LOGO_URL = '/static/favicon.svg'
DEFAULT_PROJECT_LOGO_FALLBACK_URL = '/static/web-app-manifest-512x512.png'

PROJECT_NAME = os.environ.get('PROJECT_NAME', DEFAULT_PROJECT_NAME)
PROJECT_DESCRIPTION = os.environ.get('PROJECT_DESCRIPTION', DEFAULT_PROJECT_DESCRIPTION)
PROJECT_REPOSITORY_URL = os.environ.get('PROJECT_REPOSITORY_URL', DEFAULT_PROJECT_REPOSITORY_URL)
PROJECT_RELEASES_API_URL = os.environ.get('PROJECT_RELEASES_API_URL', DEFAULT_PROJECT_RELEASES_API_URL)
PROJECT_LOGO_URL = os.environ.get('PROJECT_LOGO_URL', DEFAULT_PROJECT_LOGO_URL)
PROJECT_LOGO_FALLBACK_URL = os.environ.get('PROJECT_LOGO_FALLBACK_URL', DEFAULT_PROJECT_LOGO_FALLBACK_URL)
OPENROUTER_APP_REFERER = os.environ.get('OPENROUTER_APP_REFERER', PROJECT_REPOSITORY_URL)
OPENROUTER_APP_TITLE = os.environ.get('OPENROUTER_APP_TITLE', PROJECT_NAME)


def manifest_description(app_name: str) -> str:
    return os.environ.get(
        'PROJECT_DESCRIPTION',
        f'{app_name} is a self-hosted AI workspace for private assistants and model routing.',
    )


def manifest_icons() -> list[dict[str, str]]:
    return [
        {
            'src': PROJECT_LOGO_URL,
            'type': 'image/svg+xml',
            'sizes': 'any',
            'purpose': 'any',
        },
        {
            'src': PROJECT_LOGO_URL,
            'type': 'image/svg+xml',
            'sizes': 'any',
            'purpose': 'maskable',
        },
        {
            'src': PROJECT_LOGO_FALLBACK_URL,
            'type': 'image/png',
            'sizes': '500x500',
            'purpose': 'any',
        },
    ]
