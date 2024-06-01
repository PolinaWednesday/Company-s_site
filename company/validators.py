from rest_framework.exceptions import ValidationError


class CompanyValidator:
    """Проверка валидации компании"""

    def __call__(self, value):

        if value.get('types_sellers') != 0 and value.get('level') == 0 and value.get('supplier') != 0:
            raise ValidationError('На нулевом уровне поставки может находиться только завод. '
                                  'Выберете корректный тип сети или удалите компанию.'
                                  )

        if value.get('types_sellers') == 0 and value.get('supplier'):
            raise ValidationError('У завода не может быть компании. '
                                  'Выберете корректный тип сети или удалите компанию.'
                                  )

        if value.get('level') is None and value.get('supplier') is None and value.get('types_sellers') is None:
            raise ValidationError(
                'Для создания компании укажите компанию и тип сети. '
                'Если вы являетесь заводом, укажите тип сети - 0.'
            )

        if value.get('types_sellers') != 0 and value.get('level') != 0 and value.get('supplier') is None:
            raise ValidationError('Вы указали тип сети, не являющегося заводом. '
                                  'Если вы не являетесь заводом, укажите вашю компанию.'
                                  )

        if value.get('types_sellers') == 0 and value.get('debt') is not None:
            raise ValidationError('У завода не может быть задолженности. '
                                  'Если вы являетесь заводом, оставьте поле задолженности пустым.'
                                  )

        if value.get('types_sellers') != 0 and value.get('level') is None and value.get('supplier') is None:
            raise ValidationError(
                'Для создания записи укажите вашю компанию. '
                'Если вы являетесь заводом, укажите тип сети - 0.'
            )

        if value.get('types_sellers') == 0 and value.get('level') != 0 and value.get('level') is not None:
            raise ValidationError(
                'Вы выбрали тип сети завод - 0. '
                'Если вы являетесь заводом, в цепочке поставок вы можете иметь только уровень - 0. '
                'Для создания записи вы можете сделать следующее: '
                '1. Не указывайте уровень и компанию, либо укажите уровень в цепочке поставки - 0. '
                '2. Если не вы являетесь заводом, укажите вашу компанию и тип сети.'
            )

        if value.get('types_sellers') is None and value.get('level') != 0 and value.get('supplier'):
            raise ValidationError(
                'Для создания компании укажите тип вашей сети.'
            )

        if value.get('level') == 0 and value.get('types_sellers') != 0:
            raise ValidationError('На нулевом уровне поставки может быть только завод. '
                                  'Если вы являетесь заводом, укажите тип сети - 0.'
                                  )

        if value.get('types_sellers') and value.get('level') is not None:
            if value.get('level') != value['supplier'].level + 1:
                raise ValidationError(
                    'Уровень компании должен быть на 1 выше уровня вашего компани. '
                    'Вы можете не выставлять уровень вручную, программа сделает это самостольно.'
                )

