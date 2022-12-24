from rest_framework import serializers
from .models import Order, OrderItems, OrderTravel, OrderItemsTravel


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'address', 'total_sum', 'items', 'card', 'last_name', 'first_name']

    def validate_card(self, card):
        if len(str(card)) != 16:
            raise serializers.ValidationError('Карта дожна содержать 16 цифр!')
        return card
                
                

    def create(self, validated_data):
        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data)
        total_sum = 0
        orders_items = []
        for item in items:
            check = OrderItems(
                order=order,
                product=item['product'],
                quantity=item['quantity']
            )
            if item['product'].quantity < item['quantity']:
                raise serializers.ValidationError('неверное количество')
            if item['product'].quantity < 3:
                item['product'].price = item['product'].price * (100 - 10) / 100
            orders_items.append(check)
            total_sum +=item['product'].price * item['quantity']
            item['product'].quantity -= item['quantity']
            item['product'].save()
        OrderItems.objects.bulk_create(orders_items)
        order.total_sum = total_sum
        order.save()
        return order




class OrderItemsTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemsTravel
        fields = ['product', 'quantity']


class OrderTravelSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True)

    class Meta:
        model = OrderTravel
        fields = ['id', 'created_at', 'address', 'total_sum', 'items', 'card', 'last_name', 'first_name']

    def validate_card(self, card):
        if len(str(card)) != 16:
            raise serializers.ValidationError('Карта дожна содержать 16 цифр!')
        return card
                
                

    def create(self, validated_data):
        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data)
        total_sum = 0
        orders_items = []
        for item in items:
            check = OrderItemsTravel(
                order=order,
                product=item['product'],
                quantity=item['quantity']
            )
            if item['product'].quantity < item['quantity']:
                raise serializers.ValidationError('неверное количество')
            if item['product'].quantity < 3:
                item['product'].price = item['product'].price * (100 - 10) / 100
            orders_items.append(check)
            total_sum +=item['product'].price * item['quantity']
            item['product'].quantity -= item['quantity']
            item['product'].save()
        OrderItemsTravel.objects.bulk_create(orders_items)
        order.total_sum = total_sum
        order.save()
        return order

