# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class AwsList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the AwsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.accounts.v1.credential.aws.AwsList
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsList
        """
        super(AwsList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Credentials/AWS'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams AwsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.accounts.v1.credential.aws.AwsInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AwsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.accounts.v1.credential.aws.AwsInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AwsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return AwsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AwsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return AwsPage(self._version, response, self._solution)

    def create(self, credentials, friendly_name=values.unset,
               account_sid=values.unset):
        """
        Create a new AwsInstance

        :param unicode credentials: The credentials
        :param unicode friendly_name: The friendly_name
        :param unicode account_sid: The account_sid

        :returns: Newly created AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        data = values.of({
            'Credentials': credentials,
            'FriendlyName': friendly_name,
            'AccountSid': account_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return AwsInstance(self._version, payload)

    def get(self, sid):
        """
        Constructs a AwsContext

        :param sid: The sid

        :returns: twilio.rest.accounts.v1.credential.aws.AwsContext
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsContext
        """
        return AwsContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AwsContext

        :param sid: The sid

        :returns: twilio.rest.accounts.v1.credential.aws.AwsContext
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsContext
        """
        return AwsContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.AwsList>'


class AwsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AwsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.accounts.v1.credential.aws.AwsPage
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsPage
        """
        super(AwsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AwsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.accounts.v1.credential.aws.AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        return AwsInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.AwsPage>'


class AwsContext(InstanceContext):
    """  """

    def __init__(self, version, sid):
        """
        Initialize the AwsContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.accounts.v1.credential.aws.AwsContext
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsContext
        """
        super(AwsContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid}
        self._uri = '/Credentials/AWS/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a AwsInstance

        :returns: Fetched AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AwsInstance(self._version, payload, sid=self._solution['sid'])

    def update(self, friendly_name=values.unset):
        """
        Update the AwsInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        data = values.of({'FriendlyName': friendly_name})

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return AwsInstance(self._version, payload, sid=self._solution['sid'])

    def delete(self):
        """
        Deletes the AwsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.AwsContext {}>'.format(context)


class AwsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the AwsInstance

        :returns: twilio.rest.accounts.v1.credential.aws.AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        super(AwsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid']}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AwsContext for this AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsContext
        """
        if self._context is None:
            self._context = AwsContext(self._version, sid=self._solution['sid'])
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a AwsInstance

        :returns: Fetched AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset):
        """
        Update the AwsInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated AwsInstance
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsInstance
        """
        return self._proxy.update(friendly_name=friendly_name)

    def delete(self):
        """
        Deletes the AwsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.AwsInstance {}>'.format(context)