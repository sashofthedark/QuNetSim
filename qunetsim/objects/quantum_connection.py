class Q_Connection:
    """
    An object that stores quantum connection details
    """
    def __init__(self, receiver_id):
        self._receiver_id = receiver_id
        self._model = Fibre_Model()         # Defaults to fibre model

    @property
    def receiver_id(self):
        """
        Receiver ID
        """
        return self._receiver_id

    @property
    def model(self):
        """
        Channel model

        Returns:
            (object) : An object containing model characteristics
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Set the channel model

        Args
            model (object) : An object containing model characteristics and parameters
        """
        self._model = model

class Fibre_Model(object):

    def __init__(self):
        self._length = 0.0
        self._alpha = 0.0

    @property
    def length(self):
        """
        Length of the channel in Km

        Returns:
            (float) : Length of the channel in Km
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Set the length of the channel

        Args:
            length (float) : Length of the channel in Km
        """
        if not isinstance(length, int) and not isinstance(length, float):
            raise ValueError("Length must be float or int")
        elif length < 0:
            raise ValueError("Length must be non-negative")
        else:
            self._length = length

    @property
    def alpha(self):
        """
        Absorption coefficient of the channel in dB/Km

        Returns:
            (float) : Absorption coefficient of the channel in dB/Km
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """
        Set the absorption coefficient of the channel

        Args:
            alpha (float) : Absorption coefficient of the channel in dB/Km
        """
        if not isinstance(alpha, int) and not isinstance(alpha, float):
            raise ValueError("Alpha must be float or int")
        elif alpha < 0 or alpha > 1:
            raise ValueError("Alpha must lie in the interval [0, 1]")
        else:
            self._alpha = alpha

    @property
    def transmission_p(self):
        """
        Transmission probability of the channel

        Returns:
            (float) : Probability that a qubit is transmitted
        """
        return 10.0**(-1.0*self._alpha*self._length/10.0)